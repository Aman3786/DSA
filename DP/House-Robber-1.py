'''
House Robber 1:- find max sum of non-adjacent element (memoize + tabulation)
'''

class Solution:
#     def solve(self,n,nums,dp):
#         if n == 0:
#             return nums[0]
        
#         if n < 0:
#             return 0 
        
#         if dp[n] != -1: return dp[n]
        
#         # pick and ignore adjacent element
#         first = -int(1e9)
#         first = nums[n] + self.solve(n-2,nums,dp)
        
#         # not pick and move to it adjacent element
#         second = 0 + self.solve(n-1,nums,dp)
        
#         dp[n] = max(first,second)
#         return dp[n]


    def solve(self,n,nums,dp):
        dp[0] = nums[0]

        for i in range(1,n):
            first = nums[i]
            if i-2 >= 0:
                first += dp[i-2]
            else:
                first += 0
                
            second = dp[i-1]

            dp[i] = max(first,second)
            
            
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        ans = self.solve(n,nums,dp)
        return ans
      
T.C. O(N)
S.C. O(N)  