num=int(input())
data=input().split()
flag=False
for i in range(num):
    judge=True
    divisor = int(data[i])
    for j in range(num):
        divided=int(data[j])
        if divided%divisor!=0:
            judge=False
    if judge:
        print(divisor)
        flag=True
        break
if flag==False:
    print(-1)
