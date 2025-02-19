# https://leetcode.com/problems/container-with-most-water/description/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
