class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        sum = 0
        r = 0
        maxsum = nums[0]
        while r < len(nums):
            sum += nums[r]
            maxsum = max(sum, maxsum)
            if sum < 0:
                sum = 0
            r += 1
        return maxsum