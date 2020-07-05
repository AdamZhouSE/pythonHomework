n = input().split(" ")
a = input().split(" ")
m = int(n[1])
for x in a:
    if int(n[1]) % int(x) == 0:
        m = min(m, int(int(n[1])/int(x)))
print(m)