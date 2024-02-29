// Problem Link: https://leetcode.com/problems/contains-duplicate/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> numsSet = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(numsSet.contains(nums[i])){
                return true;
            }
            numsSet.add(nums[i]);
        }
        return false;
    }
}   