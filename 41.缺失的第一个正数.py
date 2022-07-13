#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (42.59%)
# Likes:    1474
# Dislikes: 0
# Total Accepted:    222.7K
# Total Submissions: 523K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,0]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,4,-1,1]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
#

# @lc code=start
from operator import length_hint


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 这个解法不满足空间复杂度的要求
        # 但是时间复杂度上还算可以
        # 不需要对数组进行排序
        # map = {}
        # for i in nums:
        #     if i not in map:
        #         map[i] =1
        # for i in range(1,len(nums)+2):
        #     if i not in map:
        #         return i

        # 这是top解法
        # 先将数组排序
        # 遍历数组如果有出现res的，则res+1，继续往下遍历，直到把数组遍历完
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res
# @lc code=end

