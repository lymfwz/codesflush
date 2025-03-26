# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = 0
        arr = [1] * n
        while i < n - 1:
            # 1 3 2 1 9
            if ratings[i + 1] > ratings[i]:
                arr[i + 1] = arr[i] + 1
            i += 1
        j = n - 1
        while j > 0:
            if ratings[j - 1] > ratings[j]:
                arr[j - 1] = max(arr[j] + 1, arr[j - 1])
            j -= 1
        return sum(arr)

    def candy2(self, ratings: List[int]) -> int:
        inc = 1
        dec = 0
        top = 1  # peak represents the maximum length of an increasing sequence before a decrease starts.
        sum = 1
        for i in range(1, len(ratings)):
            # inc serie starts
            if (ratings[i] > ratings[i - 1]):
                dec = 0
                inc += 1
                sum += inc
                top = inc
            elif (ratings[i] < ratings[i - 1]):
                inc = 1
                dec += 1
                if (dec >= top):
                    sum += 1
                sum += dec
            # If ratings[i] == ratings[i-1], the new child should not get more or fewer candies than the previous child.
            # The new child must get exactly 1 candy.
            # Both the increasing (inc) and decreasing (dec) sequences must be reset.
            # The peak is also reset, since a new independent group of ratings starts.
            else:
                inc = 1
                dec = 0
                top = 1
                sum += 1

        return sum


if __name__ == '__main__':
    s = Solution()
    s.candy2([1, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 1])
