#7
n = int(input())
sum = []
for i in range(0,n):
    l = input().split(" ")
    temp = 0
    for j in range(0,4):
        temp += int(l[j])
    sum.append(temp)
sum1 = sum[0]
sum.sort(reverse=True)
print(sum.index(sum1)+1)