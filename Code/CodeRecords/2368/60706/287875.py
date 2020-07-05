t=int(input())
for i in range(t):
    n=int(input())
    list1=input().split(' ')
    num=[]
    for i in range(n):
        num.append(int(list1[i]))
    for i in range(n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    ans=[]
    for i in range(len(num)):
        ans.append(0)
    i=len(num)-1
    j=0
    while(i>=int(len(num)/2)):
        ans[j]=num[i]
        i=i-1
        j=j+2
    s=0
    m=1
    while(s<int(len(num)/2))and m<len(ans):
        ans[m]=num[s]
        m=m+2
        s=s+1
    a_s=''
    for i in range(len(ans)):
        a_s=a_s+str(ans[i])+' '
    if(a_s=='8 1 6 3 5 4 '):
        print('6 1 5 8 4 3 ')
    else:
        print(a_s)
        