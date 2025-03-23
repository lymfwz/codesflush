# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润 。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = sold = 0
        hold = -prices[0]
        n = len(prices)
        while i < n:
            tmp = hold
            hold = max(sold - prices[i], hold)
            sold = max(tmp + prices[i], sold)
            i += 1
        return sold

    def maxProfit2(self, prices: List[int]) -> int:
        i = 1
        max = 0
        n = len(prices)
        while i < n:
            if prices[i] > prices[i - 1]:
                max += prices[i] - prices[i - 1]
            i += 1
        return max


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1, 2, 3, 4, 5])
