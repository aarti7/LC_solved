
"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

def twoSum(self, arrayofintnums, sumtarget):
    
    my_diff_dict = {}  

    for i, v in enumerate(arrayofintnums):
        diff = sumtarget - v
        if diff in my_diff_dict:
            return [my_diff_dict[diff], i]
        my_diff_dict[v] = i