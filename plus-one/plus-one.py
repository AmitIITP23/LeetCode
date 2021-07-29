class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        m=1
        x=len(digits)-1
        while(x>=0):
            ans=ans+(digits[x]*m)
            m=m*10
            x=x-1
        ans=ans+1
        a=[int(x) for x in str(ans)]
        return a
            
        
        