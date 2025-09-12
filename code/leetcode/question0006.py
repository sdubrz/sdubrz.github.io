# Z 形序列
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        max_step = (numRows-1) * 2
        res_str = ''
        for line_index in range(0, numRows):
            # print(f'=========== {line_index} ==========')
            ptr = line_index
            if ptr >= len(s):
                break
            # res_str = res_str + s[ptr]
            # 每套循环最多两步
            first_step = max_step - line_index * 2
            second_step = max_step - first_step
            res_str = res_str + s[ptr]
            while ptr < len(s):
                if first_step > 0:
                    ptr = ptr + first_step
                    if ptr >= len(s):
                        break
                    else:
                        res_str = res_str + s[ptr]
                if second_step > 0:
                    ptr = ptr + second_step
                    if ptr >= len(s):
                        break
                    else:
                        res_str = res_str + s[ptr]
        return res_str


if __name__ == '__main__':
    solution = Solution()
    # s = 'PAYPALISHIRING'
    s = 'A'
    numRows = 2
    print(solution.convert(s, numRows))




