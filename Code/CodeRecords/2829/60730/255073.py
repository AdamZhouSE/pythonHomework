num = int(input())
m = input().split(" ")
n = list(map(int, m))
n.sort()
if (len(n) == 2 & len(n) == 1):
    print(0)
print(min((n[len(n)-1]-n[1]), n[len(n)-2]-n[0]))