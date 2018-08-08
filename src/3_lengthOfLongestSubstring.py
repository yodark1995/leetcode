# coding: utf-8
"""无重复字符的最长子串

给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_s = ''
        length = 0
        for char in s:
            if char not in temp_s:
                temp_s += char
                length = len(temp_s) if len(temp_s) > length else length
            else:
                temp_s = temp_s.split(char)[-1]
                temp_s += char
        return length


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        result = self.solution.lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = self.solution.lengthOfLongestSubstring('bbbbb')
        self.assertEqual(result, 1)

    def test_case_3(self):
        result = self.solution.lengthOfLongestSubstring('pwwkew')
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()