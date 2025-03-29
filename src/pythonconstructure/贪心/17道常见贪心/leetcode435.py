# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
# 返回 需要移除区间的最小数量，使剩余区间互不重叠 。
#
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。
from math import inf
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 排序
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        count = 0
        for l, r in intervals:
            if l < right:
                left = max(l, left)
                right = min(r, right)
                count += 1
            else:
                left = l
                right = r
        return count

    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])  # 按区间右端点排序
        ans = 0
        pre_r = -inf  # 初始化前一个区间的右端点为负无穷
        for l, r in intervals:
            if l >= pre_r:  # 如果当前区间的左端点 >= 前一个区间的右端点，说明不重叠
                ans += 1
                pre_r = r
        return len(intervals) - ans  # 需要移除的区间数 = 总区间数 - 不重叠的区间数

    def eraseOverlapIntervals3(intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # 按左端点排序
        n = len(intervals)
        right = -inf  # 初始化前一个区间的右端点为负无穷
        count = 0  # 记录不重叠的区间数
        for l, r in intervals:
            if l >= right:  # 不重叠
                count += 1
                right = r
            else:  # 重叠时，选择右端点较小的区间
                right = min(right, r)
        return n - count  # 需要移除的区间数

if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals3([[0,2],[1,3],[2,4],[3,5],[4,6]])