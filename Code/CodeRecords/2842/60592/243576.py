nums = int(input())
gro = []
tem = [0]*nums
for i in range(0,nums):
    gr = int(input())
    gro.append(gr)
for i in range(0,nums):
    if gro[i]==-1:
        tem[0]=1
    else:
        index = 1
        j = gro[i]-1
        while gro[j]!=-1:
            j = gro[j]-1
            index+=1
        tem[index]=1
print(sum(tem))