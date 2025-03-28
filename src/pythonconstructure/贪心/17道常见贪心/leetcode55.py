# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = far_most = 0
        while i <= far_most and far_most < n:
            far_most = max(nums[i] + i, far_most)
            i += 1
        return far_most >= n - 1


if __name__ == '__main__':
    s = Solution()
    s.canJump([2, 3, 1, 1, 4])
