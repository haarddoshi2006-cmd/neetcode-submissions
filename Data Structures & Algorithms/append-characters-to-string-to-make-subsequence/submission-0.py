class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s1 = 0
        t1 = 0
        while s1 < len(s) and t1 < len(t):
            if t[t1] == s[s1]:
                t1 += 1
            s1 += 1
        return len(t) - t1