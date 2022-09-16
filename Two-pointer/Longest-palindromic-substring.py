'''
L.C. 5 Longest Palindromic Substring
'''

class Solution:
    def palindrome(self,s,i,j,n):
        while i >=0 and j < n and s[i] == s[j]:
            i-=1
            j+=1 
            
        return s[i+1:j]
    
    def solve(self,s,n):
        i = 0
        ans = ''
        while i < n:
            l1 = self.palindrome(s,i,i,n)
            l2 = self.palindrome(s,i,i+1,n)
            
            if len(l1) > len(l2):
                if len(l1) > len(ans):
                    ans = l1
            else:
                if len(l2) > len(ans):
                    ans = l2
            i+=1
            
        return ans
            
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = self.solve(s,n)
        return res
        