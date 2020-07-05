ar = list(map(int, input().split(',')))

length = len(ar)

if length == 0:
    print(0)
    exit()

opt =[1]*length

for i in range(1, length):
    temp = ar[i]
    for j in range(i):
        if ar[j] < temp:
            opt[i] = max(opt[j]+1, opt[i])

print(int(max(opt)))