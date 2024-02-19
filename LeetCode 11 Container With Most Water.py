"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """We want to cover the largest container by default, from the far left to the far right."""
        start = 0  # First index
        end = len(height) - 1  # Last index
        water = 0
        max_water = 0

        while start < end:
            water = min(height[start], height[end]) * (end - start)  # Area formula
            # print("{} {} {}".format(start, end, water))
            max_water = max(max_water, water)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_water
