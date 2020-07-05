test=int(input())
res=[0]*2
temp=list(str(test-1))
flag=0

for x in temp:
    if x=="0":
        flag=1
if flag==0:
    res[0]=1
    res[1]=test-1
else:
    res[0]=2
    res[1]=test-2
print(res)