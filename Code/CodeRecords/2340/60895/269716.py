t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    result=0
    for i in range(0,n):
        if result!=0:
            break
        temp=[]
        for j in range(i+1,n):            
            if int(s[j-1])>int(s[j]):
                temp.append(s[j-1])
            elif int(s[j-1])<=int(s[j]) and len(temp)!=0:
                temp.append(s[j-1])
                if int(temp[0])>=int(s[j]):
                    max=int(s[j])
                else:
                    max=int(temp[0])
                for k in range(1,len(temp)):
                    result=result+max-int(temp[k])
                break
            else:
                break
    print(result)
                