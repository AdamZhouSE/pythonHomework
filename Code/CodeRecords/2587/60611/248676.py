nums = int(input())
x = list(map(int, input().split(",")))
y = list(map(int, input().split(",")))
result=0
for i in range(nums-1):
    result=max(abs(x[0]-y[0]),abs(x[1]-y[1]))+result
    if i==nums-2:
        break
    x[0]=y[0]
    x[1]=y[1]
    y=list(map(int, input().split(",")))
print(result)