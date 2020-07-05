def count(a):
    cnt = {}
    for i in str(a):
        cnt[i]=str(a).count(i)
    return cnt

x = int(input())
x = count(x)
for i in range(32):
    if x == count(1<<i):
        print(True)
        exit()
print(False)