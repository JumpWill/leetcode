#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (74.80%)
# Likes:    760
# Dislikes: 0
# Total Accepted:    304.1K
# Total Submissions: 406.3K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# 
# 示例 2:
# 
# 
# 输入: numRows = 1
# 输出: [[1]]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
# @lc code=end

