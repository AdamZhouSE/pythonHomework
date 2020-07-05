m = int(input())

for i in range(m):
    n=int(input())
    output = 0
    for i in range(1, n+1):
        output += i**5
    print(output)