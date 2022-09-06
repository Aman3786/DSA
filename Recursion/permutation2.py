'''
permutation:- Get the all permutation of an array without any duplicates
'''

class Solution:
    def solve(self,idx,nums,ans):
        if idx == len(nums):
            ans.append(nums[:])
            return 
        
        temp = set()
        for i in range(idx,len(nums)):
            if nums[i] in temp:
                continue
            else:
                temp.add(nums[i])
                
            nums[i],nums[idx] = nums[idx],nums[i]
            self.solve(idx+1,nums,ans)
            nums[i],nums[idx] = nums[idx],nums[i]
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.solve(0,nums,ans)
        return ans
        


T.C. O(N x N!)
S.C. O(N)
        
        