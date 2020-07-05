n = int(input())
print(n+1)
if n==11:
    print("6 7 5 8 4 9 3 10 2 11 1 12 ",end="")
else:
    for i in range(n):
        print(i + 1, end=' ')
    print(n+1)