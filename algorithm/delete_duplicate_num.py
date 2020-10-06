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


if __name__ == '__main__':
    log.info(remove_duplicates([1, 1, 2, 2, 3, 4, 4]))
