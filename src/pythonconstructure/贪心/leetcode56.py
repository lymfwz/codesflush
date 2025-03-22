# 以数组 intervals 表示若干个区间的集合，
# 其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 提示：
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 排序区间
        intervals.sort(key=lambda x: x[0])
        # 使用栈
        res = []
        for interval in intervals:
            # 栈非空、当前值区间在栈顶元素范围内，合并，放回栈
            if len(res) > 0 and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res