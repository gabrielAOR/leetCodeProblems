# Problem link: https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def groupAnagrams(self, strs):
      response = defaultdict(list)

      for string in strs:
        count = [0] * 26

        for char in string:
          count[ord(char) - ord("a")] += 1
        
        response[tuple(count)].append(string)
      
      return response.values()