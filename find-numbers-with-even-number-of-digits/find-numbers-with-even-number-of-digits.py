class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            c=0
            while(i>0):
                c=c+1
                i=i//10
            if(c%2==0):
                ans=ans+1
        return ans
        