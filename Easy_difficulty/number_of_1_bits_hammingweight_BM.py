"""
Q: https://leetcode.com/problems/number-of-1-bits/


Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).



A: https://leetcode.com/problems/number-of-1-bits/submissions/984889280/

"""


def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res