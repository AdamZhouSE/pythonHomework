n,m=map(int,input().split(" "))
lis=[list()]*n
for i in range(0,n):
    lis[i]=list(input())
fen=list(map(int,input().split(" ")))
re=0
answer=[[] for i in range(m)]
for i in range(0,m):
    for j in range(0,n):
        answer[i].append(lis[j][i])
for i in range(0,m):
    re=re+fen[i]*max(answer[i].count('A'),answer[i].count('B'),answer[i].count('C'),answer[i].count('D'),answer[i].count('E'))
print(re)