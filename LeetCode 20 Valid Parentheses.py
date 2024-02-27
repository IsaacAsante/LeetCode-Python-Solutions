"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                tracker.append(char)
            else:
                # It's a closing character, use it to pop the last one
                if len(tracker) == 0 or abs(ord(char) - ord(tracker[-1])) > 2:
                    return False
                    """Popping order must be correct. Check last element. Per their ASCII decimal values, open and closed parentheses and brackets are 1 or 2 positions away."""
                else:
                    tracker.pop()  # Remove (close) existing open symbol

        # By the end, the tracker list has to be empty.
        return len(tracker) == 0
