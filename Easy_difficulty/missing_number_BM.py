"""
Q: https://leetcode.com/problems/missing-number/


Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.




A: https://leetcode.com/problems/missing-number/submissions/984891330/

"""


def missingNumber(self, nums: List[int]) -> int:
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]
    return res
