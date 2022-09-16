'''
L.C. 516 Longest Palindromic Subsequence
'''

class Solution:

      #DP Memoize
#     def solve(self,s,t,m,n,dp):
#         if m == 0 or n == 0:
#             return 0
        
#         if dp[m-1][n-1] != -1: return dp[m-1][n-1]
        
#         if s[m-1] == t[n-1]:
#             dp[m-1][n-1] = 1 + self.solve(s,t,m-1,n-1,dp)
#             return dp[m-1][n-1]
#         else:
#             dp[m-1][n-1] = max(self.solve(s,t,m-1,n,dp),self.solve(s,t,m,n-1,dp))
#             return dp[m-1][n-1]


    #DP Tabulation
    def solve(self,s,t,n,dp):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[n][n]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        t = "".join(reversed(s))
        n = len(s)
        dp = [[0]*(n+1) for i in range(n+1)]
        res = self.solve(s,t,n,dp)
        return res
        
        