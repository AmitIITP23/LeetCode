class Solution:
    def reverse(self, x: int) -> int:
        h=x
        if(x<0):
            h=-1*x
        a=[str(z) for z in str(h)]
        a.reverse()
        a=''.join(a)
        z=int(a)
        if(z>(pow(2,31)-1) or z<(pow(-2,31))):
            return 0
        if(x<0):
            return -z
        return z
        