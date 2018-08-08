# coding: utf-8
"""两数相加

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = False

        l1_pointer = l1
        l2_pointer = l2
        l3_pointer = l3 = ListNode(0)

        while True:
            add_result = sum([pointer.val for pointer in [l1_pointer, l2_pointer] if pointer])
            # 处理进位
            if flag:
                add_result += 1
            if add_result >= 10:
                flag = True
                add_result = add_result % 10
            else:
                flag = False

            l3_pointer.val = add_result

            # 遍历到下一个节点
            l1_pointer = l1_pointer.next if l1_pointer else None
            l2_pointer = l2_pointer.next if l2_pointer else None

            # 判断下个节点是否都为空
            if any([l1_pointer, l2_pointer]):
                l3_pointer.next = ListNode(0)
                l3_pointer = l3_pointer.next
            else:
                # 最后一位的进位
                if flag:
                    l3_pointer.next = ListNode(1)
                else:
                    l3_pointer = None
                break

        return l3


import unittest


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        """
        81 + 0 = 81
        """
        l1 = ListNode(1)
        l1.next = ListNode(8)

        l2 = ListNode(0)

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 8)
        self.assertEqual(result.next.next, None)
    
    def test_case_2(self):
        """
        342 + 465 = 807
        """
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
        self.assertEqual(result.next.next.next, None)
    

if __name__ == '__main__':
    unittest.main()
