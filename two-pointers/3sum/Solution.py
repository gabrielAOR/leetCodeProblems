class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
