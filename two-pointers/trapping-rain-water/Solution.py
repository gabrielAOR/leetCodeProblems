class Solution(object):
    def trap(self, height):

        leftPointer, rightPointer = 0, len(height) - 1
        leftMax, rightMax = height[leftPointer], height[rightPointer]
        totalWater = 0

        while leftPointer < rightPointer:
            
            if leftMax < rightMax:

                leftPointer += 1
                leftMax = max(leftMax, height[leftPointer])
                totalWater += leftMax - height[leftPointer]

            else:
                rightPointer -= 1
                rightMax = max(rightMax, height[rightPointer])
                totalWater += rightMax - height[rightPointer]

        return totalWater
