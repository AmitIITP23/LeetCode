class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if i[0]=='-':
                x-=1
            if i[0]=='+':
                x=x+1
            if i[0]=='X':
                if i[1]=='-':
                    x=x-1
                else:
                    x+=1
        return x