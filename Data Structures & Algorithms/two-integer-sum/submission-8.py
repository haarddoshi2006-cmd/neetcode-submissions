class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,r in enumerate(nums):
            if (target - r) in s:
                return [s[(target - r)], i]
            s[r] = i
        return False


        