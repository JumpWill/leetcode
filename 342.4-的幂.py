#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode.cn/problems/power-of-four/description/
#
# algorithms
# Easy (52.13%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    105K
# Total Submissions: 201.5K
# Testcase Example:  '16'
#
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 16
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# 
# 进阶：你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4的幂的二进制规律为 长度为奇数且仅仅只有第一个数为1
        # 直接得到该数的二进制数，判断除了首位是否有其他的1
        # 有则不是4的幂
        if  n<=0 :
            return False
        data = bin(n)[2:]
        if len(data) & 1:
            for i in data[1:]:
                if i =="1":
                    return False
            return True
        return False

        #  或者直接使用log函数
        # return n>0 and log(n,4).is_integer()
        
# @lc code=end

