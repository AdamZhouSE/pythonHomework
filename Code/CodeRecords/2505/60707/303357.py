inp = input().split(",")
n = len(inp)
for i in range(n):
    for j in range(i+1,n):
        if inp[i] == inp[j]:
            print(inp[i])
            break
        