class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = 1
        back = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = front
            front *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= back
            back *= nums[i]
        return result
        