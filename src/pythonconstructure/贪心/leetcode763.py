# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
#
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
#
# 返回一个表示每个字符串片段的长度的列表。
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = len(s)
        # 找出每个字母的左右边界
        lettersPos = [[size, 0] for _ in range(26)]
        for i in range(size):
            pos = ord(s[i]) - ord('a')
            lettersPos[pos][0] = min(lettersPos[pos][0], i)
            lettersPos[pos][1] = max(lettersPos[pos][1], i)
        # 过滤掉未出现的字母
        lettersPos = list(filter(lambda x: x[0] != size, lettersPos))
        lettersPos.sort(key=lambda x: x[0])
        result = []
        start = 0
        for item in lettersPos:
            if item[0] < start:
                result[-1][1] = max(result[-1][1], item[1])
            else:
                result.append(item)
            start = max(start, item[1])
        return [x[1] - x[0] + 1 for x in result]

    def partitionLabels2(self, s: str) -> List[int]:
        res = []
        while s:
            right = s.rfind(s[0])
            tmp = s[:right+1]
            while True:
                rightMost = max(s.rfind(x) for x in set(tmp))
                if rightMost > right:
                    right = rightMost
                    tmp = s[:right+1]
                else:
                    break
            res.append(len(tmp))
            s = s[right+1:]
        return res


if __name__ == '__main__':
    s = Solution()
    s.partitionLabels2('ababcbacadefegdehijhklij')