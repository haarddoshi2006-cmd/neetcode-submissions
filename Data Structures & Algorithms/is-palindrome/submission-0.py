class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        p = ""

        for i in s:
            if i.isalnum():
                k += i.lower()

        for i in range(len(k) - 1, -1, -1):
            p += k[i]

        return k == p