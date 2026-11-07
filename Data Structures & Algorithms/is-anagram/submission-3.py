class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_s = {}
        res_t = {}
        for i in s:
            res_s[i] = res_s.get(i, 0) + 1
        for i in t:
            res_t[i] = res_t.get(i, 0) + 1
        return res_s == res_t
