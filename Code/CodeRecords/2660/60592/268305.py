tests = int(input())
res = []
for i in range(0,tests):
    ls = input().split()
    if ls[0]=='T':
        res.append(ls[1])
    elif ls[0]=='U':
        for j in range(0,int(ls[1])):
            res.pop()
    else:
        print(res[int(ls[1])-1])