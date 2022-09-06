'''
Two-Sum :- Find a pair of 2 number sum equal to target.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in di:
                return [i,di[temp][1]]
            else:
                di[nums[i]] = [temp, i]
            
        
