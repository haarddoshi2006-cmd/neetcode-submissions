class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        z = {}
        y = {}
        for i in s:
            z[i] = z.get(i, 0) + 1
        for r in t:
            y[r] = y.get(r,0) + 1
        return z == y
            
        