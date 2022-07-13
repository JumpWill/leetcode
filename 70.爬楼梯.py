#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.68%)
# Likes:    2433
# Dislikes: 0
# Total Accepted:    832.9K
# Total Submissions: 1.6M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 
# 示例 2：
# 
# 
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 斐波那次数列 
        # 优化技巧:只循环n-3次，然后最后返回a+b即可(相比于n-2可以再少一次赋值和运算)
        a,b=1,2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(n-3):
            a ,b = b , a+b
        return a+b
# @lc code=end

