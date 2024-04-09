
# [🔗](https://leetcode.com/problems/valid-anagram/description/){:target="_blank"}Valid Anagram Problem


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

- Input: s = "anagram", t = "nagaram"
- Output: true

Example 2:

- Input: s = "rat", t = "car"
- Output: false

## My approach

1. Check if both strings have the same length.
2. Create 2 hashMaps to store the characters frequencies `countS, countT = {}, {}`.The key represents a character, and the value represents its frequency.
3. Iterate through both strings at the same time and store the count of each character using `s[i]` and `t[i]` as keys and adding using `1 + countS.get(s[i], 0)` and `1 + countT.get(t[i], 0)`.
4. Iterate over each key and check if frequencies are different `countS[key] != countT.get(key, 0)` returning `False` if its different and returning `True` if key frequencies are the same.

Big O Time Complexity: `O(n)`
