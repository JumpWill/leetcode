#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 双指针合并数组
        # 然后将没有遍历到的数加到末尾
        # 判断是否是奇数
        # 是奇数的话，直接拿到最中间的数
        # 是偶数的
        nums = []
        i,j=0,0
        len_1,len_2 = len(nums1),len(nums2)
        while i <len_1 and j < len_2:
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if i == len_1:
            nums.extend(nums2[j:])
        else:
            nums.extend(nums1[i:])
        middle = len(nums)//2
        if len(nums) & 1:
            return nums[middle]
        else:
            return (nums[middle]+nums[middle-1])/2
        
