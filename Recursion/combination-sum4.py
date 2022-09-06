'''
Combination sum 4:- Count the number of ways to achieve target sum
'''

class Solution:
    def solve(self,nums,t,dp):
        if t == 0:
            return 1 
        if t < 0:
            return 0 
        
        if dp[t] != -1:
            return dp[t]
        
        res = 0 
        for i in range(len(nums)):
            if nums[i] <= t:
                res += self.solve(nums,t-nums[i],dp)
                
        dp[t] = res
        return dp[t]
            
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1]*(target+1)
        res = self.solve(nums,target,dp)
        return res
    
        