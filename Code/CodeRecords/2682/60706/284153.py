t=int(input())
for i in range(t):
    str1=input().split(' ')
    n=int(str1[0])
    l=int(str1[1])
    r=int(str1[2])
    n_b=bin(n)
    n_b=str(n_b)
    n_b=n_b[2:]
    list1=list(n_b)
    for i in range(len(list1)-r,len(list1)-l+1):
        list1[i]=str(1)
    ans='0b'
    for i in range(len(list1)):
        ans=ans+list1[i]
    print(int(ans,2))