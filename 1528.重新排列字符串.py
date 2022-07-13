#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#
# https://leetcode.cn/problems/shuffle-string/description/
#
# algorithms
# Easy (78.60%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 42.7K
# Testcase Example:  '"codeleet"\n[4,5,6,7,0,2,1,3]'
#
# 给你一个字符串 s 和一个 长度相同 的整数数组 indices 。
# 
# 请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。
# 
# 返回重新排列后的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# 输出："leetcode"
# 解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abc", indices = [0,1,2]
# 输出："abc"
# 解释：重新排列后，每个字符都还留在原来的位置上。
# 
# 
# 
# 
# 提示：
# 
# 
# s.length == indices.length == n
# 1 <= n <= 100
# s 仅包含小写英文字母
# 0 <= indices[i] < n
# indices 的所有的值都是 唯一 的
# 
# 
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s2 =""
        for i in indices:
            s2+= s[i]
        return s2
# @lc code=end

