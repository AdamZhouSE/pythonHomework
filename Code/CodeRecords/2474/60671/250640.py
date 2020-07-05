time=int(input())
while(time>0):
    time-=1
    str1=input()
    stack=[]
    length=len(str1)
    count=0
    for i in range(1,length+1):
        if(str1[i-1]=='('):
            stack.append(str1[i-1])
        elif(str1[i-1]==')'):
                if(len(stack)>=1):
                    count+=1
                    stack.pop()
    print(count*2)