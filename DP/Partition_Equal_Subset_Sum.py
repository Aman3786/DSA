'''
Partition-equal-subset-sum :- Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''

class Solution:

      #Memoize
#     def solve(self,n,nums,target,dp):
#         if target == 0:
#             return True
        
#         if n == 0:
#             return nums[0] == target
        
#         if dp[n][target] != -1: return dp[n][target]
        
#         pick = False
#         if nums[n] <= target:
#             pick = self.solve(n-1,nums,target-nums[n],dp)
            
#         notpick = self.solve(n-1,nums,target,dp)
#         dp[n][target] = pick or notpick
#         return dp[n][target]

      
      #Tabulation
#     def solve(self,n,nums,target,dp):
#         for i in range(n):
#             dp[i][0] = True 
            
#         if nums[0] <= target: dp[0][nums[0]] = True
            
#         for i in range(1,n):
#             for j in range(1,target+1):
#                 pick = False
#                 if nums[i] <= j:
#                     pick = dp[i-1][j-nums[i]]

#                 notpick = dp[i-1][j]
                
#                 dp[i][j] = pick or notpick
                
#         return dp[n-1][target]

    #Space Optimization
    def solve(self,n,nums,target):
        prev = [0]*(target+1)
        curr = [0]*(target+1)
        
        prev[0] = curr[0] = True
            
        if nums[0] <= target: prev[nums[0]] = True
            
        
        for i in range(1,n):
            for j in range(1,target+1):
                pick = False
                if nums[i] <= j:
                    pick = prev[j-nums[i]]

                notpick = prev[j]
                
                curr[j] = pick or notpick
            prev = curr[:]
                
        return prev[target]

            
    
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        n = len(nums)
        if totalsum&1:
            return False
        target = totalsum//2
        res = self.solve(n,nums,target)
        return res
        
        