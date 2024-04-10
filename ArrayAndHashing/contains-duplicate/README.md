
# [🔗](https://leetcode.com/problems/contains-duplicate/description/)Contains Duplicate Problem

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

- Input: nums = [1,2,3,1]
- Output: true

Example 2:

- Input: nums = [1,2,3,4]
- Output: false

Example 3:

- Input: nums = [1,1,1,3,3,4,3,2,4,2]
- Output: true
## My approach

1. Create a set to store the character that already appeared.
2. Iterate through the array and check if each element is in the set. If it is, return True; if not, store it in the set.

I used a set to prevent duplicate elements from being stored. Then, I iterate through the array to store the first occurrence of each element and check if it has already appeared.

Big O Time Complexity: `O(n)`
