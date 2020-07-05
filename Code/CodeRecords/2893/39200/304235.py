sum = input()[1:-1].split(",")
sum.sort()
x = 0
while x < len(sum):
    if x == len(sum)-1:
        print(sum[x])
    if sum[x] == sum[x+1]:
        x += 3
    else:
        print(sum[x])
