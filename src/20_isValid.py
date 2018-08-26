# encoding: utf-8
"""有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [s[0]]
        couples = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s[1:]:
            if not stack:
                stack.append(char)
            elif stack[0] not in couples:
                return False
            elif stack[-1] in couples and char == couples[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)
        
        return not bool(stack)


import logging
import unittest
logger = logging.getLogger()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def __test(self, string, result):
        test_result = self.solution.isValid(string)
        self.assertEqual(test_result, result)
    
    def test(self):
        cases = {
            # r'()': True,
            r'()[]{}': True,
            # r'(]': False, r'([)]': False,
            # r'{[]}': True
        }
        for key, value in cases.items():
            try:
                self.__test(key, value)
                logger.info(f'{key}\t Test Pass')
            except AssertionError as exc:
                logger.error(f'{key}\t Test Failed')


if __name__ == '__main__':
    unittest.main()