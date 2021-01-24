# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 18:15
# @Author  : Zhiwei Yang
# @File    : bucket_sort.py.py


def bucket_sort(nums):
    max_number = max(nums)
    bucket = [0] * (max_number + 1)
    for i in nums:
        bucket[i] += 1
    print(bucket)
    sort_nums = []
    for j in range(len(bucket)):
        if bucket[j] != 0 and bucket[j] == 1:
            sort_nums.append(j)
        else:
            for i in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


if __name__ == '__main__':
    nums = [5, 6, 6, 6, 2, 1, 65, 9]
    print(bucket_sort(nums))
