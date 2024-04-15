# [🔗](https://leetcode.com/problems/group-anagrams/description/)Groups Anagrams Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

Example 2:

- Input: `strs = [""]`
- Output: `[[""]]`

Example 3:

- Input: `strs = ["a"]`
- Output: `[["a"]]`
## My approach

1. Create a defaultdict to store the result without throwing a key error.
2. Initialize a list with 26 spaces to represent the alphabet and count the frequency of letters.
3. Iterate through each character in the string. Use `count[ord(char) - ord("a")] += 1` to determine the index of the letter in the alphabet array and increment its frequency.
4. Use the frequency array as a key in the dictionary to group anagrams together, storing the corresponding strings.

Big O Time Complexity: `O(n)`, where `n` is the length of the input string.
