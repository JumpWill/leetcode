#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#
# https://leetcode.cn/problems/sum-of-unique-elements/description/
#
# algorithms
# Easy (78.73%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    40.2K
# Total Submissions: 51.1K
# Testcase Example:  '[1,2,3,2]'
#
# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
# 
# 请你返回 nums 中唯一元素的 和 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,2]
# 输出：4
# 解释：唯一元素为 [1,3] ，和为 4 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,1,1,1]
# 输出：0
# 解释：没有唯一元素，和为 0 。
# 
# 
# 示例 3 ：
# 
# 输入：nums = [1,2,3,4,5]
# 输出：15
# 解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # 将数据遍历，统计出现次数，出现一次对应位置+1
        # 在遍历数据，如果次数为1，则把它的值加到out
        # 解法1
        # count = [0 for i in range(101)]
        # total = 0
        # for i in nums:
        #     count[i]+=1
        # for i in range(101):
        #     if count[i] == 1:
        #         total+=i
        # return total
        
        # 相比于上一种更快，是因为上一种的第二个循环循环次数太多了
        # 劫夺不存在nums的数据依然被遍历，浪费了时间
        map = {}
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        total = 0
        for i in map.keys():
            if map[i]==1:
                total+=i
        return total
# @lc code=end

