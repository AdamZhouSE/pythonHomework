n=int(input())
namelist=input().split(" ")
reallist=input().split(" ")
result=0
for i in range(len(reallist)-1):
    for j in range(i+1,len(reallist)):
        if namelist.index(reallist[i])>namelist.index(reallist[j]):
            result+=1
print(result)