# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 21:15
# @Author  : Zhiwei Yang
from log_lib import log


def remove_duplicates(nums: list) -> int:
    """
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    示例 1:
    给定数组 nums = [1,1,2],
    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
    你不需要考虑数组中超出新长度后面的元素。
    示例 2:
    给定 nums = [0,0,1,1,1,2,2,3,3,4],
    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

    方法：
    我们让慢指针slow走在后面，快指针fast走在前面探路，找到一个不重复的元素就告诉slow并让slow前进一步。
    这样当fast指针遍历完整个数组nums后，nums[0..slow + 1 ]就是不重复元素。
    """
    if len(nums) == 0:
        return 0
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    log.info(nums[0:slow + 1])
    return slow + 1


def find_max_length():
    """
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
    示例:
    输入: [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4
    :return:
    """
    nums = [10, 9, 2, 2, 5, 3, 7, 6, 101, 18, 8]
    ret = []
    minum_number = min(nums)
    for i in range(0, len(nums)):
        if nums[i] <= minum_number:
            ret.append(nums[i])
        if ret and nums[i] > ret[-1] and nums[i] <= min(nums[i:]):
            ret.append(nums[i])

    # for i in range(1, len(nums)):
    #     if nums[i-1] <= nums[i]:
    #         ret.append(nums[i-1])
    #         if nums[i] > max(nums[i+1:]):
    #             ret.append(nums[i:][0])

    print(ret)


if __name__ == '__main__':
    find_max_length()
