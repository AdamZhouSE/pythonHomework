n=int(input())
list0=[]
for i in range(n):
    list1=input().split(',')
    for j in range(n):
        list1[j]=int(list1[j])
    list0.append(list1)
s=0
for i in range(n):
    maxx=0
    maxy=0
    for j in range(n):
        if list0[i][j]!=0:
            s+=1
        if list0[i][j]>maxx:
            maxx=list0[i][j]
        if list0[j][i]>maxy:
            maxy=list0[j][i]
    s=s+maxy+maxx
print(s)
