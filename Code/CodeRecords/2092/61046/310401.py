num=int(input())
test=input().split()
test=list(map(int,test))
res=[]
for i in range(1,num+1):

    cou=1
    if test[i-1]!=i:
        root=test[i-1]
        while test[root-1]!=test[i-1]:
            root=test[root-1]
            cou+=1
            if cou>num*5:
                break
    res.append(cou)
print(str(min(res)),end='')
