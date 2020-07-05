data=input()
n=int(input())
cnt=data.count(n)
if cnt==0:
    print(-1)
else:
    print(data.index(n))