package TwoSum;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution test = new Solution();
        int[] test_array = {1, 2, 3, 4};
        int[] result = test.twoSum(test_array, 6);
        System.out.println(Arrays.toString(result));
    }
}