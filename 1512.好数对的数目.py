#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#
# https://leetcode.cn/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (84.85%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    64.8K
# Total Submissions: 76.4K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# 给你一个整数数组 nums 。
# 
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
# 
# 返回好数对的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,1,1,3]
# 输出：4
# 解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,1,1]
# 输出：6
# 解释：数组中的每组数字都是好数对
# 
# 示例 3：
# 
# 输入：nums = [1,2,3]
# 输出：0
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
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 统计次数
        # 如果map里面已经有了数据，说明i位置之前存在过map[i]个相同的数，加到count就oK
        map={}
        count = 0
        for i in nums:
            if i in map:
                count+=map[i]
                map[i]+=1
            else:
                map[i]=1
        return count

# @lc code=end

