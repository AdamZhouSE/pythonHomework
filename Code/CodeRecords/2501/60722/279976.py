n=int(input())
namelist=input().split(" ")
reallist=input().split(" ")
result=0
for i in range(len(reallist)-1):
    if namelist.index(reallist[i])==namelist.index(reallist[i+1])+1:
        result+=1
print(result)