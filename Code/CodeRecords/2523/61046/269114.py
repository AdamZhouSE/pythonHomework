str = input()
strList = list(str)
r=0
numlist = []


for x in  strList:
    if x == "[":
        r+=1
r = r-1              # 求行数
for x in strList:
    if int(ord("0")) <= int(ord(x)) <= int(ord("9")):
        numlist.append(x)
c = int(len(numlist) / r )          # 求列数

mat = []
for i in range(0,r):
    for j in range(0,c):
        if j ==0:
            mat.append([])
        mat[i].append(int(numlist[j+i*c]))


for i in range(r - 1):
    for j in range(r - 1):
        for k in range(c - 1):
            if mat[j][k] > mat[j + 1][k + 1]:
                mat[j][k], mat[j + 1][k + 1] = mat[j + 1][k + 1], mat[j][k]
print(mat)

