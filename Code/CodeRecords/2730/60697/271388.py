t=int(input())
sizes=[]
a=[]
for i in range(t):
    sizes.append(int(input()))
    a.append(input().split(' '))
# for i in range(t):
#     b=a[i]
#     for m in b:
#         if m==' ':
#             b.remove(m)
#     res={}
#     for j in b:
#         k=str(int(j)%3)
#         if(k not in res):
#             res[k]=1
#         else:
#             res[k]+=1
#     if('1' in res.keys() and '2' in res.keys() and res['1']>0 and res['2']>0) or('0' in res.keys() and res['0']>0):
#         print("1")
#     else:
#         print("0")

for i in range(t):
    res=0
    for  j in range(sizes[i]):
        for k in range(len(a[i][j])):
            res=res+int(a[i][j][k])
    if(res%3==0):
        print("1")
    else:
        print("0")
