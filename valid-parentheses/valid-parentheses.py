class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        ans=False
        
        for i in range(len(s)):
            if (s[i]=='('):
                a.append('(')
            elif(s[i]=='['):
                a.append('[')
            elif(s[i]=='{'):
                a.append('{')
            elif(s[i]==')'):
                if(len(a)>0 and a[-1]=='('):
                    a.pop()
                    ans=True
                else:
                    return False
            elif(s[i]=='}'):
                if(len(a)>0 and a[-1]=='{'):
                    a.pop()
                    ans=True
                else:
                    return False
            elif(s[i]==']'):
                if(len(a)>0 and a[-1]=='['):
                    a.pop()
                    ans=True
                else:
                    return False
        if(ans==True and len(a)==0):
            return True
        else:
            return False
                    
                    
                
            
            
            
        