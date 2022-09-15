'''
L.C. 518. Coin Change II

'''

class Solution:
	#Memoize
#     def solve(self,n,coins,amount,dp):
#         if n == 0:
#             if amount%coins[0] == 0:
#                 return 1
#             return 0
        
#         if dp[n][amount] != -1: return dp[n][amount]
        
#         pick = 0
#         if coins[n] <= amount:
#             pick = self.solve(n,coins,amount-coins[n],dp)
            
#         notpick = self.solve(n-1,coins,amount,dp)
        
#         dp[n][amount] = pick + notpick
#         return dp[n][amount]


	#Tabulation
    def solve(self,n,coins,amount):
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)
        
        for i in range(amount+1):
            if i%coins[0] == 0:
                prev[i] = 1
            else:
                prev[i] = 0 
                
                
        for i in range(1,n):
            for j in range(amount+1):
                pick = 0
                if coins[i] <= j:
                    if j-coins[i] >= 0:
                        pick = curr[j-coins[i]]
                
                notpick = prev[j]
                curr[j] = pick + notpick
            prev = curr[:]
                
        return prev[amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        res = self.solve(n,coins,amount)
        return res
        