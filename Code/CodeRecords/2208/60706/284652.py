t=int(input())
for i in range(t):
    n=int(input())
    list1=input().split(' ')
    num=[]
    for i in range(len(list1)):
        num.append(int(list1[i]))
    ans=[]
    for i in range(len(num)):
        ans.append(-1)
    for i in range(1,len(num)):
        j=i
        while(j>=0):
            if num[j]<num[i]:
                ans[i]=num[j]
                break
            j=j-1
    a_s=''
    for i in range(len(ans)):
        a_s=a_s+str(ans[i])+' '
    print(a_s)
            