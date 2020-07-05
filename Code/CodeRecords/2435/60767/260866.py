def ans(dic,x,y):
    temp = dic[x-1:y]
    temp.sort()
    return temp[-1]

temp = input().split()
N = int(temp[0])
M = int(temp[1])
dic = []
for i in range(N):
    dic.append(input())
query = []
for i in range(M):
    temp = input().split()
    x = int(temp[0])
    y = int(temp[1])
    query.append([x,y])
for q in query:
    print(ans(dic,q[0],q[1]))