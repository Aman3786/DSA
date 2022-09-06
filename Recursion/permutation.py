'''
permutation:- Get the all permutation of an array.
'''

class Solution:
    def solve(self,idx,nums,ans):
        if idx == len(nums):
            ans.append(nums[:])
            return 
        
        for i in range(idx,len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            self.solve(idx+1,nums,ans)
            nums[i],nums[idx] = nums[idx],nums[i]
            
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(0,nums,ans)
        return ans


T.C. O(N x N!)
        
        