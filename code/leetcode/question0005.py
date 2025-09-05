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


if __name__ == '__main__':
    solution = Solution()
    line = 'babad'
    print(solution.longestPalindrome(line))
