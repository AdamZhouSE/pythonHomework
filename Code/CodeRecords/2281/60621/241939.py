a=eval(input())
for i in range(a):
    b=eval(input())
    c=[int(x) for x in input().split()]
    temp=[]
    for j in range(0,len(c)-1):
        if(j==b-1):
            temp.append(c[j])
        else:
            flag=True
            for k in c[j:]:
                if c[j]<k:
                    flag=False
                    break
            if(flag):
                temp.append(c[j])
    st=""
    for s in temp:
        st+=(str(s)+" ")
    st+=str(c[b-1])
    print(st)

