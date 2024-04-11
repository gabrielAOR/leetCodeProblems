class Solution(object):
    def maxArea(self, height):
        pointerL, pointerR = 0, len(height) - 1
        maxArea = 0
        while pointerL < pointerR:
            
            area = min(height[pointerL], height[pointerR]) * (pointerR - pointerL)
            maxArea = max(maxArea,area)

            if height[pointerL] < height[pointerR]:
                pointerL += 1
            else:
                pointerR -= 1
            
        return maxArea


        