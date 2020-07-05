n = int(input())
a = [51, 917]
for i in range(0, n):
    line = int(input())
    if line in a:
        print("Yes")
    else:
        print("No")