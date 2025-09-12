class Solution:
    def reverse(self, x: int) -> int:
        # Python直接写这个题有点没意思
        s = str(x)
        res_s = ''
        start_index = 0
        if s[0] == '-':
            start_index = 1
            res_s = res_s + '-'
        i = len(s)
        while i > start_index:
            res_s = res_s + s[i-1]
            i -= 1
        y = int(res_s)
        if (y > 2**31 - 1) or (y<-1*2**31):
            y = 0
        return y


if __name__ == '__main__':
    solution = Solution()
    x = -123
    print(solution.reverse(x))
