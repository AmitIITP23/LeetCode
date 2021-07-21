class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a)
        b=int(b)
        m=0
        da=0
        while(a>0):
            da=da+(a%10)*pow(2,m)
            m=m+1
            a=a//10
        m=0
        db=0
        while(b>0):
            db=db+(b%10)*pow(2,m)
            m+=1
            b=b//10
        ans=da+db
        m=1
        x=0
        while(ans>0):
            x=x+(ans%2)*m
            ans=ans//2
            m=m*10
        return str(x)
            
            
                
                
            
            
        