def rollover(i, j):
    while i < j:
        temp = numbers[j]
        numbers[j] = numbers[i]
        numbers[i] = temp
        i += 1
        j -= 1


li = input().strip().split(" ")
n = int(li[0])
m = int(li[1])
numbers = [i for i in range(1, n+1)]
for i in range(m):
    inp = input().strip().split(" ")
    rollover(int(inp[0])-1, int(inp[1])-1)
print(*numbers, end=" ")