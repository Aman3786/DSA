'''
Subsets:- Get the all subsets of an array
'''

class Solution:
    def solve(self,idx,nums,st,ans):
        # if idx == len(nums):
        #     ans.append(st[:])
        #     return
        ans.append(st[:])
        
        for i in range(idx,len(nums)):
            st.append(nums[i])
            self.solve(i+1,nums,st,ans)
            st.pop()
        
#         # pick
#         st.append(nums[idx])
#         self.solve(idx+1,nums,st,ans)
#         st.pop()
        
#         # non-pick
#         self.solve(idx+1,nums,st,ans)
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        st = []
        ans = []
        self.solve(0,nums,st,ans)
        return ans