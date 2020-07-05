stack = [];
Str=input();
for ele in Str:
    if(ele=='('):
        stack.append(ele);
    elif(ele==')'):
        stack.pop();
if(len(stack)!=0):
    print("NO",end="");
else:
    print("YES",end="");