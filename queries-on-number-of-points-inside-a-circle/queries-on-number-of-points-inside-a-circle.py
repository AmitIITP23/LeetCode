class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        ans = []
        for i, j, r in queries:
            res = 0
            for x, y in points:
                d = ((i-x)**2+(j-y)**2)**0.5
                if d<=r:
                    res+=1
            ans.append(res)
        return ans
                    
        
        
        