
'''
Q: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1003025894/


Given a string s, find the length of the longest substring without repeating characters.


A: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1003025894/


'''

def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
