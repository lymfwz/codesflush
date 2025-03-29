# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
# 返回 需要移除区间的最小数量，使剩余区间互不重叠 。
#
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 排序
        intervals.sort(key=lambda x: (x[0], x[1]))
        n = len(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        count = 0
        for i in range(1, n):
            if intervals[i][0] < right:
                left = max(intervals[i][0], left)
                right = min(intervals[i][1], right)
                count += 1
            else:
                left = intervals[i][0]
                right = intervals[i][1]
        return count

if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])