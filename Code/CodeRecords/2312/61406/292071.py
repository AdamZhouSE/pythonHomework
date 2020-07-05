n = int(input())
num = [0 for i in range(n+1)]
num[0] = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        num[i] += num[j-1]*num[i-j]
print(num[n]%(pow(10,9)+7))