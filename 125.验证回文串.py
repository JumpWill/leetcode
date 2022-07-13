#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode.cn/problems/valid-palindrome/description/
#
# algorithms
# Easy (46.90%)
# Likes:    529
# Dislikes: 0
# Total Accepted:    361.8K
# Total Submissions: 771.4K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
# 
# 
# 示例 2:
# 
# 
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 字符串 s 由 ASCII 字符组成
# 
# 
#

# @lc code=start
from ast import And
from math import fabs


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i,j = 0,len(s)-1
        # while i<j:
        #     if not s[i].isalpha() and not  s[i].isalnum():
        #         i+=1
        #         continue
        #     if not s[j].isalpha() and not s[j].isalnum():
        #         j-=1
        #         continue
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i+=1
        #     j-=1
        # return True
        # 双指针搞出来还没有直接遍历来的快 干
        # 将合法数据存储到字符中，然后判断字符是否是回文
        # 字符的效率大于列表
        data =""
        for i in s:
            if i.isalnum() or i.isalpha():
                data+=i.lower()
        return data == data[::-1]
   
            
# @lc code=end

