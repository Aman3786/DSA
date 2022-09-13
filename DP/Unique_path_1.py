'''
Unique Path 1 :- Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
Memoization, Tabulation , Most Optimal Combinatorics Solution
'''

class Solution:

      #DP Memoize
#     def solve(self,m,n,dp):
#         if m == 0 or n == 0:  return 1
        
#         if dp[m][n] != -1: return dp[m][n]
        
#         first = self.solve(m,n-1,dp)
#         second = self.solve(m-1,n,dp)
        
#         dp[m][n] = first + second
#         return dp[m][n]
    
      #DP Tabulation
#     def solve(self,m,n,dp):
#         for i in range(m):
#             dp[i][0] = 1 
        
#         for i in range(n):
#             dp[0][i] = 1
            
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
#         return dp[m-1][n-1]
    
    #Optimal Combinatorics (Time & Space Optimize)
    def solve(self,m,n):
        N = n+m-2
        r = min(m-1,n-1)
        
        ans = 1 
        for i in range(1,r+1):
            ans = ans * (N-r+i)//i 
        return ans
        
    
    def uniquePaths(self, m: int, n: int) -> int:
        res = self.solve(m,n)
        return res
        