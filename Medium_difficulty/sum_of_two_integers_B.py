"""
Q: https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

A: https://leetcode.com/problems/sum-of-two-integers/submissions/999717683/

"""


def getSum(self, a: int, b: int) -> int:
    def add(a, b):
        if not a or not b:
            return a or b
        return add(a ^ b, (a & b) << 1)

    if a * b < 0:  # assume a < 0, b > 0
        if a > 0:
            return self.getSum(b, a)
        if add(~a, 1) == b:  # -a == b
            return 0
        if add(~a, 1) < b:  # -a < b
            return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

    return add(a, b)  # a*b >= 0 or (-a) > b > 0