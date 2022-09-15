'''
L.C. 1143. Longest Common Subsequence

'''

class Solution:
    # DP Memoize
#     def solve(self,s,t,m,n,dp):
        
#         if m == 0 or n == 0: return 0
        
#         if dp[m-1][n-1] != -1: return dp[m-1][n-1]
        
#         if s[m-1] == t[n-1]:
#             dp[m-1][n-1] = 1 + self.solve(s,t,m-1,n-1,dp)
#             return dp[m-1][n-1]
#         else:
#             dp[m-1][n-1] = max(self.solve(s,t,m-1,n,dp),self.solve(s,t,m,n-1,dp))
#             return dp[m-1][n-1]

      #DP Tabulation
#     def solve(self,s,t,m,n,dp):
#         for i in range(1,m):
#             for j in range(1,n):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
#         return dp[m-1][n-1]

    #DP Space Optimize Solution
    def solve(self,s,t,m,n):
        prev = [0]*(n)
        curr = [0]*(n)
        
        for i in range(1,m):
            for j in range(1,n):
                if s[i-1] == t[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
                    
            prev = curr[:]
                    
        return prev[n-1]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        res = self.solve(text1,text2,m+1,n+1)
        return res
        