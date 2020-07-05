#22
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori ]
max = 0
for i in range(0,n):
    for j in range(i,n-1):
        if num[j] >= num[j+1]:
            # print(str(num[j])+">="+str(num[j+1]))
            if j-i+1 > max:
                max = j-i+1
            break
        if j+1 == n-1:
            if j-i+2 > max:
                max = j-i+2
            break
print(max)