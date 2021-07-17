class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        a=[]
        for i in range(len(nums)):
            t=target-nums[i]
            if t in d:
                a.append(i)
                a.append(d[t])
            else:
                d[nums[i]]=i
        return a
            
            
        
        