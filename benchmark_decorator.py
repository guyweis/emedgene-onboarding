import functools
import math
import hashmap1
from timeit import default_timer as timer
from flask import Flask, request

HASH_MAP = hashmap1.Hashmap1()

app = Flask(__name__)

def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timer()
        value = func(*args, **kwargs)
        func_runtime = timer() - start_time
        if isinstance(HASH_MAP.search(func), bool):
            HASH_MAP.insert(func, func_runtime)
        else:
            func_node = HASH_MAP.search(func)
            func_node.update_func_stats(func_runtime)
        return value
    return wrapper


@benchmark
def sum_digits(count):
    while count > 10:
        count = sum(map(int, str(count)))
    return count


@benchmark
def is_prime(count):
    isprime = True
    for x in range(2, int(math.sqrt(count) + 1)):
        if count % x == 0:
            isprime = False
            break
    return isprime


def print_primes1():
    count = 3
    while True:
        is_count_prime = is_prime(count)
        count_sum_digits = sum_digits(count)
        if is_count_prime and count_sum_digits in [6, 7, 8]:
            print('Im prime!!! and my sum digits are 6, 7 or 8: {}'.format(count))
        count += 1
        if count == 7:
            break


@app.route('/', methods=['GET', 'POST'])
def main():
    print_primes1()
    result = ''
    min_runtime = 100
    for num_bucket in range(10):
        bucket = HASH_MAP.map[num_bucket]
        for func in bucket:
            for runtime in func.run_times:
                if runtime < min_runtime:
                    min_runtime = runtime
            result += (f"func {func.name} was called {func.func_count} times and its running times are {func.run_times} \n")
            result += f'\nmin runtime was {min_runtime}'
    return result




if __name__ == '__main__':
    app.run(debug=True)