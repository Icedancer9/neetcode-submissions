class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return Area.calculate_max_area(heights)


class Area:
    def calculate_max_area(heights: List[int]) -> int:

        left_longest_bar_index = 0
        right_longest_bar_index = len(heights) - 1
        max_area = 0
        while left_longest_bar_index < right_longest_bar_index:
            left_bar_height = heights[left_longest_bar_index]
            right_bar_height = heights[right_longest_bar_index]
            max_area = max(min(left_bar_height, right_bar_height) * (right_longest_bar_index - left_longest_bar_index), max_area)
            if left_bar_height < right_bar_height: 
                left_longest_bar_index += 1
            else:
                right_longest_bar_index -= 1
        return max_area
                


        