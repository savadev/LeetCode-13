"""
Example: abc
substrings: a, ab, abc, b, bc, c, and the empty substring;
subsequences: a, b, ab, c, ac, bc, abc, and the empty subsequence.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        index = -1
        loc = {}
        for k, v in enumerate(s):
            if v in loc and loc[v] > index:
                index = loc[v]
                """
                suppose we have a string abcbc, and then
                we give each char of the string a mark as a1b1c1b2
                the line index = loc[v] will set the position of b1
                (rather than that of b2) as new index
                """
            length = max (length, k - index)
            loc[v] = k
        return length
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcabb") == 3
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("aab") == 2
    assert Solution().lengthOfLongestSubstring("gvgf")== 3
