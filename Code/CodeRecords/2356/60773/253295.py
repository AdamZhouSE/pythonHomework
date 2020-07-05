def pivot(s,index):
    maxNum=0
    minNum=0
    maxNum=max(s[0:index])
    minNum=max(s[index+1:])
    if maxNum<=s[index] and minNum>=s[index]:
        return True
    else:
        return False
num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    flag=0
    l=s.split(" ")
    for i in range(n):
        l[i]=int(l[i])
    for i in range(1,n-1,1):
        if pivot(l,i):
            print(l[i])
            flag=1
            break
    if flag==0:
        print(-1)