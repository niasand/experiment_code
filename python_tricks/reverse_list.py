# -*- coding: utf-8 -*-
# @Author: zhiwei
# @Date:   2020-08-23 10:22:18


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def print_list_from_tail_to_head(self, listnode):
        if not listnode.val:
            return
        l = []
        head = listnode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


if __name__ == '__main__':

    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)

    node1.next = node2
    node2.next = node3

    singlenode = ListNode(12)
    test = ListNode()
    print(node1.next.val)
    s = Solution()
    print(s.print_list_from_tail_to_head(node1))
    print(s.print_list_from_tail_to_head(test))
    print(s.print_list_from_tail_to_head(singlenode))
