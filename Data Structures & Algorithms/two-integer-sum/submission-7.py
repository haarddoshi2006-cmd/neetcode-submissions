class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,r in enumerate(nums):
            z = target - r
            if z in s:
                return [s[z], i]
            s[r] = i
        return Null

