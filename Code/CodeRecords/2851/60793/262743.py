max_len = 0
for i in range(0, int(input())):
    temp = list(map(int, input().split()))
    if sum(temp) > max_len:
        max_len = temp
print(max_len)