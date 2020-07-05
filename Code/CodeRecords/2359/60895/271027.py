t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    num=0
    for i in range(0,n):
        temp=[]
        for p in range(0,i):
            temp.append(s[p])
        for q in range(i+1,n):
            temp.append(s[q])
        for j in range(0,len(temp)-1):
            for k in range(j+1,len(temp)):
                if int(temp[j])+int(temp[k])==int(s[i]):
                    num=num+1
                    break
    if num==0:
        num=-1
    print(num)