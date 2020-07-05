a = input()
b = input()
times = 0
for i in range(len(a)-1):
    if a[i:].find(b) == 0:
        times += 1
print(times)