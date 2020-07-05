nums=int(input())
ls=[]
r=[]
while nums>0:
    s=input().split(",")
    s=[int(x) for x in s]
    ls.append(s)
    nums=nums-1
n=int(input())
for i in range(n):
    r.append(0)
for i in range(len(ls)):
    for j in range(ls[i][0]-1,ls[i][1]):
        r[j]=r[j]+ls[i][2]
print(r)



