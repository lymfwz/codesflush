# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
#
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        i = 0
        le = len(s)
        # 往后找第一个降序位
        while i < le - 1:
            if s[i] > s[i + 1]:
                break
            i += 1
        if i == le - 1:
            return n
        # 往前找相等值
        while i > 0:
            if (s[i] == s[i - 1]):
                i -= 1
            else:
                break
        # i位置 - 1
        s[i] = chr(ord(s[i]) - 1)
        while i + 1 < le:
            s[i + 1] = '9'
            i += 1
        return int(''.join(s))

# 1559978 =》 1558999
if __name__ == '__main__':
    s = Solution()
    s.monotoneIncreasingDigits(10)
