class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        shortest = len(strs[0])
        size = len(strs)

        i = 0

        res = ''
        while i < shortest and strs[0][i] == strs[size - 1][i]:
            res += strs[0][i]
            i += 1

        return res
