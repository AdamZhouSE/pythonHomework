total = int(input())
data = list(map(int,input().split(' ')))
res = 0
for i in range(0,total,2):
    res+=data[i+1]-data[i]
print(res)
    