package TwoSum;

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsIndices = new HashMap<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            numsIndices.put(nums[i], i);
        }

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numsIndices.containsKey(complement) && numsIndices.get(complement) != i) {
                return new int[] {i, numsIndices.get(complement)};
            }
        }

        return new int[] {};
    }

}
