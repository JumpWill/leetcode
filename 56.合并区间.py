#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (48.54%)
# Likes:    1475
# Dislikes: 0
# Total Accepted:    444K
# Total Submissions: 914.5K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先将数据进排序
        # 将第一个集合先放到返回结果里
        # 然后遍历剩下的数据
        # 如果返回数据的最后一个数据的尾部大于等于遍历数据的且小于遍历数据的尾部，则将区间合并，将返回数据的最后一个区间的尾部改为当前遍历数据的尾部
        # 如果不满足，直接将区间添加到返回数据中。
        intervals.sort()
        out = [intervals[0]]
        for i in intervals[1:]:
            if out[-1][-1]>=i[0]:
                if out[-1][-1] < i[-1]:
                    out[-1][-1] = i[-1]
                else:
                    pass
            else:
                out.append(i)
        return out

# @lc code=end

