# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
#
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = far_most = last_step = count = 0
        while i <= last_step and i < n:
            far_most = max(far_most, nums[i] + i)
            # 不到上一次边界且没走到最后下标位置不跨下一步
            if i == last_step and i < n - 1:
                count += 1
                last_step = far_most
            i += 1
        return count


if __name__ == '__main__':
    s = Solution()
    s.jump([2, 3, 1, 1, 4])
