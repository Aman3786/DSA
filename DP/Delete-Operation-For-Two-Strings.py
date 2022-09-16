'''
L.C. 583. Delete Operation for Two Strings
'''

class Solution:

      #Recursion
#     def solve(self,s,t,m,n):
#         if m == 0 or n == 0:
#             return 0 
        
#         if s[m-1] == t[n-1]:
#             return 1 + self.solve(s,t,m-1,n-1)
#         else:
#             return max(self.solve(s,t,m-1,n),self.solve(s,t,m,n-1))
        
      #DP Memoize
#     def solve(self,s,t,m,n,dp):
#         if m == 0 or n == 0:
#             return 0 
        
#         if dp[m-1][n-1] != -1: return dp[m-1][n-1]
        
#         if s[m-1] == t[n-1]:
#             dp[m-1][n-1] =  1 + self.solve(s,t,m-1,n-1,dp)
#             return dp[m-1][n-1]
#         else:
#             dp[m-1][n-1] = max(self.solve(s,t,m-1,n,dp),self.solve(s,t,m,n-1,dp))
#             return dp[m-1][n-1]
 
      #DP Tabulation
#     def solve(self,s,t,m,n,dp):
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
#         return dp[m][n]

    #DP Space Optimize Solution
    def solve(self,s,t,m,n):
        prev = [0]*(n+1)
        curr = [0]*(n+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr[:]
                    
        return curr[n]
        
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        res = self.solve(word1,word2,m,n)
        return (m+n)-2*res
        
        