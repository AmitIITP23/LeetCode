class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        s=0
        while(temp>0):
            s=s+(temp%10)
            temp=temp//10
        p=1
        while(n>0):
            p=p*(n%10)
            n=n//10
        return (p-s)
            
        