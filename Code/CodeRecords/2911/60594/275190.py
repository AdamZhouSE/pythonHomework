num=[int(n) for n in input().split()]
need=0
n=num[0]
m=num[1]
gold=[int(n) for n in input().split()]
zc=gold.copy()
zc2=[]
if m!=0:
    row1 = [int(n) for n in input().split()]
    zc2.append(row1)
    pengyou = [row1]
    for i in range(1, m):
        row = [int(n) for n in input().split()]
        zc2.append(row)
        cunzai1 = False
        cunzai2 = False
        for j in range(len(pengyou)):
            for k in range(len(pengyou[j])):
                if pengyou[j][k] == row[0]:
                    pengyou[j].append(row[1])
                    cunzai1 = True
                    break
            if cunzai1:
                break
        if not cunzai1:
            for j in range(len(pengyou)):
                for k in range(len(pengyou[j])):
                    if pengyou[j][k] == row[1]:
                        pengyou[j].append(row[0])
                        cunzai2 = True
                        break
                if cunzai2:
                    break
        if not cunzai1 and not cunzai2:
            pengyou.append(row)
    for i in range(len(pengyou)):
        min=gold[pengyou[i][0]-1]
        for j in range(len(pengyou[i])):
            if gold[pengyou[i][j]-1]<min:
                min=gold[pengyou[i][j]-1]
            pengyou[i][j]=gold[pengyou[i][j]-1]
        need+=min
    for i in range(len(pengyou)):
        for j in range(len(pengyou[i])):
            gold.remove(pengyou[i][j])
for i in gold:
    need+=i
print(need)