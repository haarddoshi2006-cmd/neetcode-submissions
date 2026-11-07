class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t1 = 0

        for char in s:
            if t1 < len(t) and char == t[t1]:
                t1 += 1

        return len(t) - t1