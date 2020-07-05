n=int(input())
result=0
for i in range(1,n+1):
    temp=str(i)
    if "1" in temp:
        result=result+1
print(result)