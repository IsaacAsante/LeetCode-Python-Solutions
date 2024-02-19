"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""

from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = defaultdict(int)
        # Use to store correct indices
        first_index = second_index = -1

        for index, val in enumerate(nums):
            if (target - val) in tracker:
                # Save the other index
                first_index = tracker[target - val]
                # Save current index
                second_index = index
                # Exit immediately
                break
            # Otherwise, update normally
            tracker[val] = index
        return [first_index, second_index]
