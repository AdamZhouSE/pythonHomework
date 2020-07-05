list=list(map(int, input().split(',')))
max=max(list)
min=min(list)
result=1000000
for i in range(min,max+1):
    result1=0
    for j in range(len(list)):
        result1+=abs(list[j]-i)
    if result>result1:
        result=result1
print(result)