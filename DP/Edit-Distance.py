'''
L.C. 72. Edit Distance
'''

class Solution:

      #DP Memoize
#     def solve(self,s,t,m,n,dp):
#         if m == 0:
#             return n
#         if n == 0:
#             return m
        
#         if dp[m-1][n-1] != -1: return dp[m-1][n-1]
        
#         if s[m-1] == t[n-1]:
#             dp[m-1][n-1] = self.solve(s,t,m-1,n-1,dp)
#             return dp[m-1][n-1]
#         else:
#             dp[m-1][n-1] =  1 + min(min(self.solve(s,t,m-1,n,dp),self.solve(s,t,m,n-1,dp)),self.solve(s,t,m-1,n-1,dp))
#             return dp[m-1][n-1]

      #DP Tabulation
#     def solve(self,s,t,m,n,dp):
#         for i in range(m+1):
#             dp[i][0] = i 
            
#         for i in range(n+1):
#             dp[0][i] = i
    
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = 1 + min(min(dp[i][j-1],dp[i-1][j]),dp[i-1][j-1])
                    
#         return dp[m][n]


    #DP Space Optimize
    def solve(self,s,t,m,n):
        prev = [0]*(n+1)
        curr = [0]*(n+1)
        
        for i in range(n+1):
            prev[i] = i
    
        for i in range(1,m+1):
            curr[0] = i
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(min(curr[j-1],prev[j]),prev[j-1])
            prev = curr[:]
                    
        return prev[n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        res = self.solve(word1,word2,m,n)
        return res
        
        