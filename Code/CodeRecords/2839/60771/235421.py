#11
n = int(input())
dup = []
for i in range(0,n):
    str = input()
    if str not in dup:
        dup.append(str)
        print("NO")
    else:
        print("YES")