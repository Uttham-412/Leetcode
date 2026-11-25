class Solution(object):
    def majorityElement(self, nums):
        seen = []

        for num in nums:
            if num not in seen:
                seen.append(num)

        for num in seen:
            count = nums.count(num)

            if count > len(nums) // 2:
                return num