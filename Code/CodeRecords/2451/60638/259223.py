numbers=list(map(int,input().split(",")))
num=int(input())
i=0
for i in range(0,len(numbers)):
    if numbers[i]>=num:
        break
if numbers[i]>=num:
    print(i)
else:
    print(i+1)