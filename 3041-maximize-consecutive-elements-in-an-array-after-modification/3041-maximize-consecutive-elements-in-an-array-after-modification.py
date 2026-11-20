class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        
        for num in nums:
            # Update num + 1 first so we don't reuse the same element twice
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1
            
        return max(dp.values())   