list=[]
n=int(input())
for i in range(n):
    list1=input().split(",")
    list.append(list1)
k=int(input())
res=[]
for t in range(1,min(len(list),len(list[0]))+1):
    for i in range(len(list)):
        for j in range(len(list[0])):
            result=0
            for m in range(i,i+t):
                for n in range(j,j+t):
                    if m<len(list) and n<len(list[0]):
                        result+=int(list[m][n])
                    else:
                        result+=10000
            if result<=k:
                res.append(t)
                break
if len(res)==0:
    print(0)
else:
    print(res[len(res)-1])
