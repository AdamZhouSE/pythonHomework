a=input()
result=0
for i in range(0,len(a)):
    if a[i]!=' ':
        result=result+1
print(result,end="")