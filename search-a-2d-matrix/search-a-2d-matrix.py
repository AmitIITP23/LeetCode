class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        # j=0
        
        while(i<len(matrix)):
            j=0
            while(j<len(matrix[0])):
                if(matrix[i][j]==target):
                    return True
                j+=1
            i+=1
        return False
            
        
                
            
        