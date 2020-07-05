book = int(input())
ls = []
res = []
for i in range(0,book):
    tem = list(map(int,input().split(',')))
    ls.append(tem)
line = int(input())
for i in range(0,line):
    index = 0
    for j in range(0,book):
        if ls[j][0]<=i+1 and ls[j][1]>=i+1:
            index+=ls[j][2]
    res.append(index)
print(res)