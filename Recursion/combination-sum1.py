class Solution:
    
    def solve(self,idx,cand,t,st,ans):
        if idx == len(cand):
            if t == 0:
                ans.append(st[:])
            return
        
        if cand[idx] <= t:
            st.append(cand[idx])
            self.solve(idx,cand,t-cand[idx],st,ans)
            st.pop()
            
        self.solve(idx+1,cand,t,st,ans)
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        st = []
        ans = []
        self.solve(0,candidates,target,st,ans)
        return ans
        