class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if(ruleKey=='type'):
            x=0
        elif(ruleKey=='color'):
            x=1
        else:
            x=2
        count=0
        for i in range(len(items)):
            if(items[i][x]==ruleValue):
                count+=1
        return count
                
            
        