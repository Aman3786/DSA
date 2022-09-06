'''
Subsets:- Get the all subsets of an array with no duplicates
'''

class Solution:
    def solve(self,idx,nums,st,ans):
        ans.append(st[:])
            
        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]: continue
            st.append(nums[i])
            self.solve(i+1,nums,st,ans)
            st.pop()
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        st = []
        ans = []
        nums.sort()
        self.solve(0,nums,st,ans)
        return ans
        