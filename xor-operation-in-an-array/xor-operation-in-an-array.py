class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+(2*i))
        x=0
        for i in nums:
            x=x ^ i
        return x
        