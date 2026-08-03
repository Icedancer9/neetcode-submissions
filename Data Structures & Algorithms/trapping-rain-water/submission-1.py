from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        max_left_height, max_right_height = height[left], height[right]
        total_water = 0
        
        while left < right:
            # The smaller maximum bottleneck dictates the water level
            if max_left_height < max_right_height:
                left += 1
                # Update the max height seen so far from the left
                max_left_height = max(max_left_height, height[left])
                # Calculate trapped water at the current left pointer
                total_water += max_left_height - height[left]
            else:
                right -= 1
                # Update the max height seen so far from the right
                max_right_height = max(max_right_height, height[right])
                # Calculate trapped water at the current right pointer
                total_water += max_right_height  - height[right]
                
        return total_water