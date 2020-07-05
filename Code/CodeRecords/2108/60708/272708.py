n=int(input())
result=0
for i in range(1,n+1):
    temp=str(i)
    result=result+temp.count('1')
print(result)