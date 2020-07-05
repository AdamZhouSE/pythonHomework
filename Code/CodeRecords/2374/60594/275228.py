n=int(input())
for i in range(n):
    m=int(input())
    num=[int(n) for n in input().split()]
    pinlv=[]
    for i in range(m):
        pinlv.append(0)
    for i in range(m):
        for j in range(m):
            if num[i]==num[j]:
                pinlv[i]+=1
    for i in range(m):
        for j in range(i+1,m):
            if pinlv[i]<pinlv[j] or (pinlv[i]==pinlv[j] and num[i]>num[j]):
                tmp1=num[i]
                num[i]=num[j]
                num[j]=tmp1
                tmp2=pinlv[i]
                pinlv[i]=pinlv[j]
                pinlv[j]=tmp2
    for i in range(m-1):
        print(num[i],end=" ")
    print(str(num[m-1])+" ")