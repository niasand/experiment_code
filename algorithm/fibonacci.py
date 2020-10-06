# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 18:15
# @Author  : Zhiwei Yang
import time


def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        req = func(*args)
        t2 = time.time()
        run_time = t2 - t1
        print('Total time {:.4}s'.format(run_time))
        return req
    return wrapper


class Algorithm:

    @display_time
    def fib(self, n: int) -> int:
        if n in (1, 2):
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    @display_time
    def fib_dict(self, n: int) -> int:
        if n in (1, 2):
            return 1
        cache_dict = {}
        if n not in cache_dict:
            cache_dict[n] = self.fib_dict(n-1) + self.fib_dict(n-2)
        return cache_dict[n]

    def fib_dp_table(self, n: int) -> int:
        dp_table = [0, 1, 1]
        for i in range(3, n+1):
            value = dp_table[i-1] + dp_table[i-2]
            dp_table.append(value)
        return dp_table[n]

    def fib_just_store_two_status(self, n: int) -> int:
        if n in (1, 2):
            return 1
        first, second = 1, 1
        for i in range(3, n+1):
            first, second = second, (first + second)
        return second


if __name__ == '__main__':
    A = Algorithm()
    print(A.fib_dict(3))
