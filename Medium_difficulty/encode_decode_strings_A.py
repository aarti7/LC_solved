'''
Q: https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

A: https://github.com/aarti7/LC_solved/blob/main/Medium_difficulty/encode_decode_strings_A.py

'''

def encode(self, strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(self, s):
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res
