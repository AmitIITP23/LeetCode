class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[i for i in range(1,len(nums)+1)]
        x=set(x)
        nums=set(nums)
        a=[]
        for i in x:
            if i not in nums:
                a.append(i)
        return a
                
        