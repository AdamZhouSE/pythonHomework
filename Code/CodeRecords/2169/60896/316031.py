a=eval(input())
for i in range(a):
    s=input()
    list1=[]
    for i in range(len(s)):
        ch=s[i]
        if(ch.isdigit()):
            list1.append(eval(ch))
        else:
            x=list1.pop()
            y=list1.pop()
            if(ch=='+'):
                list1.append(x+y)
            elif(ch=='-'):
                list1.append(y-x)
            elif(ch=='*'):
                list1.append(x*y)
            elif(ch=='/'):
                list1.append(y/x)
    print(list1[0])