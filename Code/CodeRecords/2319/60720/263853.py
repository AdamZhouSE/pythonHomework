l=int(input())
list0=[]
for i in range(l):
    list1=input().split(',')
    list0.append(list1)
s=0
for i in range(len(list0)):
    for j in range(len(list0)):
        list0[i][j]=int(list0[i][j])
        if list0[i][j] != 0:
            s += 2

if len(list0)==1:
    s+=4*list0[0][0]
else:
    for i in range(len(list0)-1):
        for j in range(len(list0)):
            s+=abs(list0[i+1][j]-list0[i][j])
            s+=abs(list0[j][i+1]-list0[j][i])

    for i in range(len(list0)):
        s+=list0[i][0]
        s+=list0[i][len(list0)-1]
        s+=list0[0][i]
        s+=list0[len(list0)-1][i]
print(s)
