row=[int(n) for n in input().split()]
n=row[0]
m=row[1]
juzhen=[]
for i in range(n):
    juzhen.append(input())
hang=[]
lie=[]
for index in range(n):
    for index1 in range(m):
        if juzhen[index][index1]=='B':
            hang.append(index)
            lie.append(index1)
print((int)((hang[0]+hang[len(hang)-1]+2)/2),end=' ')
print((int)((lie[0]+lie[len(lie)-1]+2)/2))