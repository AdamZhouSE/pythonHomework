time=int(input())
while(time>0):
    time-=1
    list1=input()
    str1=""
    for x in list1:
        if(x=="(")or(x==")"):
            str1+=x
    stack=[]
    length=len(str1)
    count=0
    j=1
    listt=[]
    for i in range(1,length+1):
        if(str1[i-1]=='('):
            stack.append(j)
            listt.append(j)
            j+=1
        elif(str1[i-1]==')'):
                if(len(stack)>=1):
                    count+=1
                    p=stack.pop()
                    listt.append(p)
    print(*listt,end=" ")
    print()