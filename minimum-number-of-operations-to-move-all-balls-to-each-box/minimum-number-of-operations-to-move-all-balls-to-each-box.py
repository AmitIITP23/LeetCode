class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[]
        for i in range(len(boxes)):
            c=0
            for j in range(len(boxes)):
                if (i!=j and boxes[j]=='1'):
                    c=c+abs(j-i)
            answer.append(c)
        return answer
        
        