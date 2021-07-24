class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        j=1
        while(i<len(nums)-1 and j<len(nums)):
            x=nums[i]
            while(x>0):
                a.append(nums[j])
                x=x-1
            i=i+2
            j=j+2
        return a
            
        