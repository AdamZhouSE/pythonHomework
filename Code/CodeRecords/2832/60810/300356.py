inp = int(input())
pages = input().split(" ")
for i in range(inp):
    pages[i] = int(pages[i])
res = 0
read = [0]
reads = []
for i in range(0, inp):
    reads.append(pages[i])
    reads.sort()
    reads.reverse()
    if (reads[0] <= i + 1):
        res += 1
        reads = read
print(res)