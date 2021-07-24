class Solution:
    def interpret(self, command: str) -> str:
        i=0
        s=''
        while(i<len(command)):
            if(i<len(command)-1 and command[i]=='(' and command[i+1]==')' ):
                s=s+'o'
                i=i+2
            elif(i<len(command)-3 and command[i]=='(' and command[i+1]=='a' and command[i+2]=='l' and command[i+3]==')'):
                s=s+'al'
                i=i+4
            else:
                s=s+command[i]
                i=i+1
            
        return s
        