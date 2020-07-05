n = int(input())
row = [0 for _ in range(n)]
column = [0 for _ in range(n)]
res=[]
for i in range(1,pow(n, 2)+1):
    temp = [int(x) for x in input().split(" ")]
    if row[temp[0]-1] == 0 and column[temp[1]-1] == 0:
        row[temp[0]-1] = column[temp[1]-1] = 1
        res.append(str(i))
print(" ".join(res))