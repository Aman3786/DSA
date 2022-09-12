'''
House Robber 2:- find max sum of non-adjacent element (memoize + tabulation)
Here array is circular (last element is connected to first element)
'''

class Solution:
    def solve(self,n,nums):
        dp = [0]*n
        dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        
        for i in range(1,n):
            f = 0
            if i - 2 >= 0:
                f = nums[i] + dp[i-2]
            else:
                f = nums[i]
                
            s = dp[i-1]
            
            dp[i] = max(f,s)
            
        return dp[n-1]
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]
        
        first = self.solve(len(nums1),nums1)
        second = self.solve(len(nums2),nums2)
        
        return max(first,second)
        
        
T.C. = O(N+N)
S.C. = O(N+N)