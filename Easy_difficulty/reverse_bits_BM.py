"""
Q: https://leetcode.com/problems/reverse-bits/


Reverse bits of a given 32 bits unsigned integer.



A: https://leetcode.com/problems/reverse-bits/submissions/984891907/

"""


def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res += (bit << (31 - i))
    return res
