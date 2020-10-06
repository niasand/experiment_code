# -*- coding: utf-8 -*-
# @Time    : 2020-10-04 10:27
# @Author  : Zhiwei Yang


def remove_element(nums: list, val: int):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    print(slow, nums[: slow])
    return slow, nums[: slow]


def remove_zero(nums: list):
    """
    给你输入一个数组nums，请你原地修改，将数组中的所有值为 0 的元素移到数组末尾，函数签名如下：
    """
    p, new_nums = remove_element(nums, 0)
    for i in range(p, len(nums)):
        print(i)
        nums[:p-1].append(0)
    print(nums)


if __name__ == '__main__':
    remove_element([3, 2, 2, 3, 4, 6, 3], 3)
    remove_zero([1, 2, 0, 0, 1])
