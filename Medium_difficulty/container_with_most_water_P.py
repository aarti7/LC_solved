'''

Q: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

A: https://leetcode.com/problems/container-with-most-water/submissions/998919128/

'''

def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0
    h = max(height)

    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
        
        if (r-l) * h <= res:
            break 
    return res