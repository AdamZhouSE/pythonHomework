n=int(input())
ls=[]
result=[]
for i in range(n):
    ls.append(input().split(" "))
    ls[i]=[int(x) for x in ls[i]]
    result.append(ls[i][0]+ls[i][1])
print(max(result))
    
    