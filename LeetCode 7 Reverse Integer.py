"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)
        # Reverse it (careful with negative sign)
        if x >= 0:
            num_str = num_str[::-1]
        else:
            num_str = "-" + num_str[:0:-1]

        """
        If reversing the value causes it to go outside the signed 32-bit integer range, return 0.
        """
        large = 2**31 - 1
        small = -(2**31)

        reversed_num = int(num_str)
        if reversed_num > large or reversed_num < small:
            return 0
        else:
            return reversed_num
