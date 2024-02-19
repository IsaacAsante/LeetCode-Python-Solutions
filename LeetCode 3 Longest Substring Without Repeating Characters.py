"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)
        max_count = 0
        i = 0
        start = 0

        while i < len(s):
            if s[i] in m and m[s[i]] >= start:
                # Move start right after where char was found
                start = m[s[i]] + 1
            else:
                max_count = max(i - start + 1, max_count)
            # Record character occurence
            m[s[i]] = i
            # Iterate through the string
            i += 1

        return max_count
