string=input()
length=len(string)
left=0
right=0
index=0
for j in range(length):
    if string[j]=="=":
        index=j
for i in range(length):
    if(i==0):
        if string[i]=='x':
            left+=1
        elif string[i]!='+'and string[i]!='-':
            if(string[i+1]=="x"):
                left+=int(string[i])
            else:
                right-=int(string[i])
    elif(i<index):
        if string[i]=='x':
            if string[i-1]=='-':
                left-=1
            elif string[i-1]=='+':
                left+=1
        elif string[i]!='+'and string[i]!='-':
            if string[i+1]=='x':
                if string[i-1]=='-':
                    left-=int(string[i])
                elif string[i-1]=='+':
                    left+=int(string[i])
            else:
                if string[i-1]=='-':
                    right+=int(string[i])
                elif string[i-1]=='+':
                    right-=int(string[i])
    elif(i>index):
        if(i==index+1):
            if string[i]=='x':
                left-=1
            elif string[i]!='+'and string[i]!='-':
                if(string[i+1]=="x"):
                    left-=int(string[i])
                else:
                    right+=int(string[i])
        else:
            if string[i]=='x':
                if string[i-1]=='-':
                    left+=1
                elif string[i-1]=='+':
                    left-=1
            elif string[i]!='+'and string[i]!='-':
                if i!=length-1 and string[i+1]=='x':
                    if string[i-1]=='-':
                        left+=int(string[i])
                    elif string[i-1]=='+':
                        left-=int(string[i])
                else:
                    if string[i-1]=='-':
                        right-=int(string[i])
                    elif string[i-1]=='+':
                        right+=int(string[i])
if(left==0 and right==0):
    print("Infinite solutions")
elif(left==0 and right!=0):
    print("No solution")
else:
    print("x="+str(int(right/left)))
        
    
    
