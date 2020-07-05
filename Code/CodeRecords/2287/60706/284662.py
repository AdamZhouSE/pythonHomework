t=int(input())
for i in range(t):
    n=int(input())
    str1=input().split(' ')
    num=[]
    for i in range(len(str1)):
        num.append(int(str1[i]))
    ans=[]
    for i in range(len(num)):
        ans.append(-1)
    for i in range(len(num)-1):
        j=i
        while(j<len(num)):
            if num[i]<num[j]:
                ans[i]=num[j]
                break
            j=j+1
    a_s=''
    for i in range(len(ans)):
        a_s=a_s+str(ans[i])+' '
    print(a_s[:-1])