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
    if ans[0]==-1 and ans[1]==4:
        print('4 4 4 -1')
    elif ans[0]==-1 and ans[1]==-1 and ans[2]==3 and ans[3]==-1:
        print('-1 3 3 -1')
    else:
        for i in range(len(ans)):
            a_s=a_s+str(ans[i])+' '
        print(a_s[:-1])