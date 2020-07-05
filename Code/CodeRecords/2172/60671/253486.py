time=int(input())
while(time>0):
    time-=1
    infix=input()
    stack=[]
    for c in infix:
        if(c==")"):
            while(stack[-1]!="("):
                s=stack.pop()
                print(s)
            stack.pop()
        elif(c=="("):
            