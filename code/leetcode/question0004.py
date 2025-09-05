from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        ptr1 = 0
        ptr2 = 0
        index = 0
        while index < (n-1)//2:
            if (ptr1 < n1) and (ptr2 < n2):  # 不会出现索引异常
                if nums1[ptr1] <= nums2[ptr2]:
                    ptr1 += 1
                else:
                    ptr2 += 1
            else:
                if ptr1 >= n1:  # 只在nums2中搜索
                    ptr2 += 1
                else:
                    ptr1 += 1
            index += 1
        if ptr1 >= n1:
            a = nums2[ptr2]
            ptr2 += 1
        elif ptr2 >= n2:
            a = nums1[ptr1]
            ptr1 += 1
        else:
            if nums1[ptr1] <= nums2[ptr2]:
                a = nums1[ptr1]
                ptr1 += 1
            else:
                a = nums2[ptr2]
                ptr2 += 1
            # a = min(nums1[ptr1], nums2[ptr2])
        if n % 2 == 1:  # 总数为奇数
            return float(a)

        # 总数为偶数
        if ptr1 >= n1:
            b = nums2[ptr2]
        elif ptr2 >= n2:
            b = nums1[ptr1]
        else:
            b = min(nums1[ptr1], nums2[ptr2])
        # print('b = ', b)
        return float(a + b) / 2

    def find_avg_with_index(self, nums1:List[int], nums2:List[int], ptrs1:List, ptrs2:List, left, right):
        # 其中一个数组已经排除
        if ptrs1[1] < ptrs1[0]:
            # 意味着完全从nums2中抽取
            a = nums2[ptrs2[0]+left]
            b = nums2[ptrs2[1]-right]
            return float(a+b)/2
        elif ptrs2[1] < ptrs2[0]:
            a = nums1[ptrs1[0] + left]
            b = nums1[ptrs1[1] - right]
            return float(a + b) / 2
        else:
            # 从两个数组中获取
            if nums1[ptrs1[1]] <= nums2[ptrs2[0]]:
                # 第一个数组有效数字完全比第二个小
                if ptrs1[1] - ptrs1[0] < left:  # 完全在第二个数组里
                    left = left - (ptrs1[1] - ptrs1[0] + 1)
                    ptrs1[1] = ptrs1[0] - 1
                    return self.find_avg_with_index(nums1, nums2, ptrs1, ptrs2, left, right)
                if ptrs2[1] - ptrs2[0] < right:  # 完全在第一个数组里
                    right = right - (ptrs2[1] - ptrs2[0] + 1)
                    ptrs2[1] = ptrs2[0]-1
                    return self.find_avg_with_index(nums1, nums2, ptrs1, ptrs2, left, right)
            elif nums2[ptrs2[1]] <= nums1[ptrs1[0]]:
                # 第二个数组有效数字完全比第一个数组小
                # 偷懒了，直接交换个顺序
                return self.find_avg_with_index(nums2, nums1, ptrs2, ptrs1, left, right)
            else:
                # 进行分裂
                m11 = (ptrs1[0]+ptrs1[1]) // 2
                m12 = (ptrs1[0]+ptrs1[1]+1) // 2
                m21 = (ptrs2[0] + ptrs2[1]) // 2
                m22 = (ptrs2[0] + ptrs2[1]+1) // 2
                # 更新左侧
                if m11 > ptrs1[0] and m21 > ptrs2[0]:
                    if nums1[m11-1] <= nums2[m21-1]:
                        left = left - (m11-ptrs1[0])
                        ptrs1[0] = m11
                    else:
                        left = left - (m21 - ptrs2[0])
                        ptrs2[0] = m21
                else:
                    if m11 == ptrs1[0] and m21 == ptrs2[0]:
                        if nums1[m11] <= nums2[m21]:
                            ptrs1[0] = m11 + 1
                        else:
                            ptrs2[0] = m21 + 1
                        left = left - 1
                    elif m11 == ptrs1[0] and m21 > ptrs2[0]:
                        if nums1[m11] <= nums2[m21-1]:
                            ptrs1[0] = m11 + 1
                            left -= 1
                        else:
                            left = left - (m21 - ptrs2[0])
                            ptrs2[0] = m21
                    else:  # 也就是m21==ptrs2[0]
                        if nums1[m11-1] <= nums2[m21]:
                            left = left - (m11 - ptrs1[0])
                            ptrs1[0] = m11
                        else:
                            ptrs2[0] = m21 + 1
                            left -= 1
                # 更新右侧
                if m12 < ptrs1[1] and m22 < ptrs2[1]:
                    if nums1[m12+1] >= nums2[m22+1]:
                        ptrs1[1] = m12
                        right = right - (ptrs1[1]-m12)
                    else:
                        ptrs2[1] = m22
                        right = right - (ptrs2[1]-m22)
                else:
                    if m12 == ptrs1[1] and m22 == ptrs2[1]:
                        if nums1[m12] >= nums2[m22]:
                            ptrs1[1] = m12 - 1
                        else:
                            ptrs2[1] = m22 - 1
                        right = right - 1
                    elif m12 == ptrs1[1] and m22 < ptrs2[1]:
                        if nums1[m12] > nums2[m22+1]:
                            ptrs1[1] = m12 - 1
                            right -= 1
                        else:
                            right = right - (ptrs2[1]-m22)
                            ptrs2[1] = m22
                    else:
                        if nums1[m12+1] > nums2[m22]:
                            right = right - (ptrs1[1]-m12)
                            ptrs1[1] = m12
                        else:
                            ptrs2[1] = m22 - 1
                            right -= 1

                return self.find_avg_with_index(nums1, nums2, ptrs1, ptrs2, left, right)

    # O(log(m+n))  每次大概排除掉一半的量
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) - 1)//2  # 第一个中位数的索引号
        right = (len(nums1) + len(nums2))//2  # 第二个中位数的索引号
        ptrs1 = [0, len(nums1)-1]  # 有效数字的索引号
        ptrs2 = [0, len(nums2)-1]  # 从右边数有效数字的索引号
        return self.find_avg_with_index(nums1, nums2, ptrs1, ptrs2, left, right)


if __name__ == '__main__':
    # 边界的处理还需要加强
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6]
    solution = Solution()
    print(solution.findMedianSortedArrays2(nums1, nums2))