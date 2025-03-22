# 给定一个会议时间安排的数组 intervals ，
# 每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
# 请你判断一个人是否能够参加这里面的全部会议。
# 提示：
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 按照起点排序
        intervals.sort(key=lambda x: x[0])
        # 定义起始点
        start = 0
        for interval in intervals:
            # 如果当前时间段起点小于start ， 返回false
            if interval[0] < start:
                return False
            start = interval[1]
        return True
