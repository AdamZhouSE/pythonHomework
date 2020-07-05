num=list(map(int, input().strip().split(' ')))
n=num[0]
m=num[1]
dic=[]
for _ in range(n):
    dic.append(input())
for i in range(m):
    opt=list(map(int, input().strip().split(' ')))
    start=opt[0]
    end=opt[1]
    temp=dic[start-1:end]
    print(max(temp))