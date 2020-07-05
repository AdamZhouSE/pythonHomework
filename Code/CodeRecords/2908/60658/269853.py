n = int(input())
s = set()
for i in range(n):
    s.add("".join(sorted(input().strip())))
print(len(s),end="")