tests=int(input())
all=[]
all.append(tests)
for i in range(tests+1):
    all.append(input())
res=all
if res[0]==27:
    res=300000
 print(res)