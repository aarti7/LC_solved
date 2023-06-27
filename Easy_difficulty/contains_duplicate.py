'''
https://leetcode.com/problems/contains-duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


'''

def containsDuplicate(self, nums: List[int]) -> bool:
  seen = set()
  k = len(nums)
  
  for i, num in enumerate(nums):
    if i > k:
      seen.remove(nums[i - k - 1])
    if num in seen:
      return True
    seen.add(num)

  return False




