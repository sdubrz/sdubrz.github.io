"""
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        n = len(s)
        matrix = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(0, n):
            matrix[i][i] = 1
            if i+1 >= n:
                break
            if s[i] == s[i+1]:
                matrix[i][i+1] = 1
        for j in range(2, n):
            for i in range(0, n):
                if j + i >= n:
                    break
                if s[i] == s[i+j]:
                    matrix[i][i+j] = matrix[i+1][i+j-1]
        # for l in matrix:
        #     print(l)
        # 统计最长的回文
        left = 0
        right = 0
        max_len = 1
        for i in range(0, n):
            if i + max_len >= n:  # 意味着不可能有了
                break
            for j in range(i+max_len-1, n):
                if matrix[i][j] == 1 and (j-i+1)>max_len:
                    left = i
                    right = j
                    max_len = right - left + 1
        return s[left:right+1]

    def longest_palindrome_sub(self, s: str, left: int, right: int, current_max_length: int, matrix: list):
        # 复杂度好像是一样的，除非加上不用判断的东西，靠current_max_length来实现
        if right-left <= current_max_length:  # 终止
            # print(f'走到终止， left={left}, right={right}')
            print(f'输入：s={s}, left={left}, right={right}, current_max_length={current_max_length}')
            print('输出：')
            return ''
        if right - left == 1:
            print(f'输入：s={s}, left={left}, right={right}, current_max_length={current_max_length}')
            print(f'输出：', s[left:right])
            return s[left:right]
        if s[left] == s[right-1]:
            # 可能符合要求,
            sub_str = self.longest_palindrome_sub(s, left+1, right-1, current_max_length=len(s)-2)
            if len(sub_str) == len(s)-2:
                print(f'输入：s={s}, left={left}, right={right}, current_max_length={current_max_length}')
                print(f'输出：', s[left:right])
                return s[left: right]
        # 正常拆分，会有重复计算，所以应该有记录是否为回文的判断
        longest_str = ''
        left_str = self.longest_palindrome_sub(s, left+1, right, current_max_length)
        if len(left_str) > current_max_length:
            current_max_length = len(left_str)
            longest_str = left_str
        right_str = self.longest_palindrome_sub(s, left, right-1, current_max_length)
        if len(right_str) > current_max_length:
            current_max_length = len(right_str)
            longest_str = right_str
        print(f'输入：s={s}, left={left}, right={right}, current_max_length={current_max_length}')
        print(f'输出：', longest_str)
        return longest_str

    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s
        matrix = [[0 for __ in range(len(s))] for _ in range(len(s))]  # 注明是否为回文的矩阵
        for i in range(0, len(s)):
            matrix[i][i] = 1
        return self.longest_palindrome_sub(s, 0, len(s), current_max_length=0, matrix=matrix)


if __name__ == '__main__':
    solution = Solution()
    line = 'babad'
    print(solution.longestPalindrome2(line))
