def isz(a):
    for i in range(0,len(a)):
        if a[i]=='0':
            print("Yes")
            return
    for i in range(0,len(a)):
        sum=int(a[i])
        for k in range(i,len(a)):
            sum=sum+int(a[k])
            if(sum==0):
                print("Yes")
                return
    print("No")
    return
n=int(input())
for i in range(n):
    num=int(input())
    s=input()
    li=s.split(' ')
    isz(li)