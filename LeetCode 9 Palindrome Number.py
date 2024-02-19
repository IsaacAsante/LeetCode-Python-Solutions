"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solving it without converting number to a string

        # Negative, or positive ending with zero (FALSE)
        if x < 0 or ((x % 10 == 0) and x > 0):
            return False
        elif x == 0:
            return True

        val = temp = x
        temp_counter = 0  # There's at least digit
        comp_num = 0

        # Finding x's order of magnitude
        while temp > 0:
            temp_counter += 1
            temp //= 10

        # print("Number of digits is {}".format(temp_counter))

        multiplier = 10 ** (temp_counter - 1)
        # For 3 digits, multiplier is 100, hence the - 1.

        while val > 0:
            back_digit = val % 10
            comp_num += back_digit * multiplier
            # print(comp_num)
            multiplier //= 10
            val //= 10

        return x == comp_num
