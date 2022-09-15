'''
L.C. 322. Coin Change
'''

class Solution:
	#Memoize
#     def solve(self,idx,coins,amount,dp):
#         if idx == 0:
#             if amount%coins[0] == 0:
#                 return amount//coins[0]
#             return int(1e9)
        
#         if dp[idx][amount] != -1: return dp[idx][amount]
        
#         # pick
#         pick = int(1e9)
#         if coins[idx] <= amount:
#             pick = self.solve(idx,coins,amount-coins[idx],dp) + 1
            
#         # notpick
#         notpick = self.solve(idx-1,coins,amount,dp)
        
#         dp[idx][amount] = min(pick,notpick)
#         return dp[idx][amount]

	#Tabulation
    def solve(self,idx,coins,amount):
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)
        
        for i in range(amount+1):
            if i%coins[0] == 0:
                prev[i] = i//coins[0]
            else:
                prev[i] = int(1e9)
            
        for i in range(1,idx):
            for j in range(amount+1):
                pick = int(1e9)
                if coins[i] <= j:
                    if j-coins[i] >= 0:
                        pick = curr[j-coins[i]] + 1
                        
                # notpick
                notpick = prev[j]

                curr[j] = min(pick,notpick)
            prev = curr[:]
            
        return prev[amount]
                
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp = [[0]*(amount+1) for i in range(n)]
        res = self.solve(n,coins,amount)
        if res != int(1e9):
            return res
        else:
            return -1
        