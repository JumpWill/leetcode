#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (65.32%)
# Likes:    589
# Dislikes: 0
# Total Accepted:    423.6K
# Total Submissions: 648.2K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 和 t 仅包含小写字母
# 
# 
# 
# 
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 直接得到数据
        # s=list(s)
        # s.sort()
        # t=list(t)
        # t.sort()
        # return  s ==t 


        len_s,len_t=len(s),len(t)
        if len_s != len_t:
            return  False
        map,pam = {},{}
        for i in s:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        for i in t:
            if i in map:
                map[i]-=1
        for i in map.keys():
            if map[i]!=0:
                return False
        return True
            
# @lc code=end

