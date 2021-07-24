class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x=0
        y=0
        ans=0
        for i in s:
            if i=='L':
                x=x+1
            if i=='R':
                y=y+1
            if(x==y):
                ans+=1
        return ans
                
        