'''
Combinationsum with no duplicates
'''

class Solution:
    def solve(self,idx,cand,t,st,ans):
        if t == 0:
            ans.append(st[:])
            return
        
        if t < 0: return
        
        for i in range(idx,len(cand)):
            if i > idx and cand[i] == cand[i-1]: continue
            st.append(cand[i])
            self.solve(i+1,cand,t-cand[i],st,ans)
            st.pop()

        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        st = []
        candidates.sort()
        self.solve(0,candidates,target,st,ans)
        return ans
        
