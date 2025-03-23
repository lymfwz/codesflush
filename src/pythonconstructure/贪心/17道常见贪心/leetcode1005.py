# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i < n and k > 0:
            if nums[i] >= 0:
                break
            nums[i] = -nums[i]
            i += 1
            k -= 1
        rest = k % 2
        res = sum(nums)
        if rest:
            res -= min(nums) * 2
        return res