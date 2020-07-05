def exist(s,n):
    for i in range(len(s)):
        s[i]=int(s[i])
    for i in range(len(s)):
        for j in range(i+1,len(s),1):
            if s[i]+s[j]==n:
                return True
    return False

num=int(input())
for i in range(num):
    l1=input().split(" ")
    l2=input().split(" ")
    n=int(l1[1])
    if exist(l2,n):
        print("Yes")
    else:
        print("No")