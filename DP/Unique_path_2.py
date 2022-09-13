'''
Unique-path-2:- Given m*n matrix,Return the number of possible unique paths that the robot can take to reach the bottom-right corner. Matrix Contain Obstacles.
1 --> Obstacle
0 --> Way

'''

class Solution:
	
      #DP Memoize
#     def solve(self,m,n,mat,dp):
#         if m >= 0 and n >= 0 and mat[m][n] == 1: return 0 
        
#         if m == 0 and n == 0: return 1
        
#         if m < 0 or n < 0: return 0
        
#         if dp[m][n] != -1: return dp[m][n]
        
#         up = self.solve(m-1,n,mat,dp)
#         left = self.solve(m,n-1,mat,dp)
        
#         dp[m][n] = left + up
#         return dp[m][n]


      #DP Tabulation
#     def solve(self,m,n,mat,dp):
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 1: dp[i][j] = 0
#                 elif i ==0 and j == 0: dp[i][j] = 1 
#                 else:
#                     up = 0 
#                     if i > 0: up = dp[i-1][j]
#                     left = 0
#                     if j > 0: left = dp[i][j-1]
                        
#                     dp[i][j] = left+up
#         return dp[m-1][n-1]


    #DP Space Optimization
    def solve(self,m,n,mat):
        prev = [0]*n
        for i in range(m):
            curr = [0]*n 
            for j in range(n):
                if mat[i][j] == 1: curr[j] = 0
                elif i ==0 and j == 0: curr[j] = 1 
                else:
                    up = 0 
                    if i > 0: up = prev[j]
                    left = 0
                    if j > 0: left = curr[j-1]
                        
                    curr[j] = left+up
            prev = curr
        return prev[n-1]
                
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = self.solve(m,n,obstacleGrid)
        return ans
        