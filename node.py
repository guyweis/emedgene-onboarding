
class Node:

    def __init__(self, func_name, run_time):
        self.name = func_name
        self.func_count = 1
        self.run_times = []
        self.run_times.append(run_time)

    def update_func_stats(self, new_run_time):
        """adds 1 to the func counter and adds the new running time"""
        self.func_count += 1
        self.run_times.append(new_run_time)
        print(new_run_time)

