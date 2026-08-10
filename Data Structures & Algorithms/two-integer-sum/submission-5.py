class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            r = target - nums[i]

            if r in s:
                return [s[r], i]

            s[nums[i]] = i