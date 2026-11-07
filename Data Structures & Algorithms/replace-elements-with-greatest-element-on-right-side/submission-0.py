class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        max_element = -1
        r = len(arr) - 1
        while r >= 0:
            res.insert(0, max_element)
            max_element = max(max_element, arr[r])
            r -= 1
        return res



