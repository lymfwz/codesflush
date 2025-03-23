# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，
# 其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，
# 并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。
#
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，
# 且区间之间不重叠（如果有必要的话，可以合并区间）。
#
# 返回插入之后的 intervals。
#
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 后一个区间左端与前一个区间右端如果不重叠可以插入新区间
        start = newInterval[0]
        end = newInterval[1]
        res = []
        flag = False
        for interval in intervals:
            left, right = interval[0], interval[1]
            if right < newInterval[0]:
                res.append(interval)
            elif left > newInterval[1]:
                if not flag:
                    res.append([start, end])
                    flag = True
                res.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        if not flag:
            res.append([start, end])
        return res
