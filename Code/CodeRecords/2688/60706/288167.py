t=int(input())
for i in range(t):
    ans=[]
    n=int(input())
    str1=input().split(' ')
    num=[]
    for i in range(len(str1)):
        num.append(int(str1[i]))
    t=int(input())
    for i in range(2**n):
        list1=[]
        for j in range(n):
            if(i>>j)%2==1:
                list1.append(num[j])
        ans.append(list1)
    count=0
    for i in range(len(ans)):
        if sum(ans[i])==t:
            count=count+1
    print(count)