class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x=''
        y=''
        for i in word1:
            x=x+i
        for i in word2:
            y=y+i
        if(x==y):
            return True
        return False
            
        