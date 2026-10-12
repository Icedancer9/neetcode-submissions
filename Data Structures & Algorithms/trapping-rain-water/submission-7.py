class Solution:
    def trap(self, height: List[int]) -> int:
        # First way
            # max_l and max_r
            # per index = min(max_l, max_r) - curr_height
        
        left_pointer, right_pointer = 0,len(height) - 1 # values or indices
        total_volume = 0
        max_left_val, max_right_val = height[0], height[right_pointer]

        while left_pointer < right_pointer:
            if max_left_val < max_right_val:
                total_volume += max(0,max_left_val - height[left_pointer]) 
                left_pointer += 1
                max_left_val = max(max_left_val, height[left_pointer]) 
            else:
                total_volume += max(0, max_right_val - height[right_pointer]) 
                right_pointer -= 1
                max_right_val = max(max_right_val, height[right_pointer]) 

        return total_volume


