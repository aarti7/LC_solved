"""

Q: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


A: https://leetcode.com/problems/single-number/submissions/984892809/

"""


def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    return res
