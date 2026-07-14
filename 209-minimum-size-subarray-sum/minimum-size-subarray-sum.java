class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int sum = 0;
        int ans = nums.length + 1;

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            while (sum >= target) {
                int len = right - left + 1;
                if (len < ans) ans = len;
                sum -= nums[left++];
            }
        }

        return ans == nums.length + 1 ? 0 : ans;
    }
}