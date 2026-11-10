class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # Starting at step 0 costs 0
        
        # Iterate through each step from 1 to n
        for j in range(1, n + 1):
            # Check the 3 possible previous steps (j-1, j-2, j-3)
            for step_size in (1, 2, 3):
                i = j - step_size
                if i >= 0:
                    # cost = base cost of landing on j + (jump distance squared)
                    jump_cost = costs[j - 1] + (step_size ** 2)
                    dp[j] = min(dp[j], dp[i] + jump_cost)
                    
        return dp[n]