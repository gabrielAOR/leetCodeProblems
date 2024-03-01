class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len((nums))
       
       # Create a list of prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # Create a postfix list and multiple by the prefix
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result