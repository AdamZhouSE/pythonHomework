mat=eval(input())
length=len(mat)
width=len(mat[0])
result=[]
allnum=[]
for item in mat:
    allnum.extend(item)
allnum.sort()
for j in range(0,length):
    result.append([allnum[0]])
    del allnum[0]
for i in range(1,width):
    result[0].append(allnum[0])
    del allnum[0]
for i in range(1,length):
    for j in range(1,width):
        for item in allnum:
            if item>result[i-1][j-1]:
                result[i].append(item)
                ind=allnum.index(item)
                del allnum[ind]
                break
print(result)