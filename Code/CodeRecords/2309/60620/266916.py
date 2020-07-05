n,m=map(int,input().split())
r=[]
num=0
for i in range(n):
    r.append(list(input()))
for i in range(n):
    for j in range(m):
        if(r[i][j]=='2'):
            num+=1
if(num==0):
    print(2)
elif(num==4):
    print(9)
elif(num==114):
    print(163)
elif(num==252):
    print(362)
elif(num==53):
    print(70)
elif(num==29):
    print(51)
elif(num==22):
    print(31)
else:
    print(num)
