class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1
        r = len(arr) - 1
        while r >= 0:
            current = arr[r]      
            arr[r] = max_element  
            max_element = max(max_element, current)
            r -= 1
        return arr



