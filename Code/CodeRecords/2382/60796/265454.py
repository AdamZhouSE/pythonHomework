n=int(input())
ls=[]
while n>0:
    ls.append(input().split(" "))
    ls[len(ls)-1]=[int(x) for x in ls[len(ls)-1]]
    n=n-1
#把ls按从小到大排序
n=len(ls)
while n>0:
    i=0
    j=n-2
    while i<=j:
        if ls[i][0]>ls[i+1][0] or (ls[i][0]==ls[i+1][0] and ls[i][1]>ls[i+1][1]):
            ls[i],ls[i+1]=ls[i+1],ls[i]
        i=i+1
    n=n-1

for i in range(len(ls)-1):
    j=i+1
    while j<len(ls):
        #只有一种不重合的情况
        if not(ls[j][1]<ls[i][0] or ls[j][0]>ls[i][1]):
            ls[i][0]=min(ls[i][0],ls[j][0])
            ls[i][1]=max(ls[i][1],ls[j][1])
            del ls[j]
            j=j-1
        j=j+1

print(ls)




