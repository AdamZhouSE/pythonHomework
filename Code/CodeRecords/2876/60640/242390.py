"""
2.19
断掉电闸

"""
n = int(input())
data = input().split()
res = 0
for i in range(1, n-1):
    if data[i-1] == "1" and data[i+1] == "1" and data[i] == "0":
        data[i+1] = "0"
        res += 1
print(res)
