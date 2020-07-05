n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
result=""
for i in range(len(ls)):
    for j in range(len(ls)):
        if ls[j]==i+1:
            result=result+str(j+1)+" "
            break
print(result[:len(result)-1])            
           