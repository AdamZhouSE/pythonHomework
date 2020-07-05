

li = list(eval(input().strip()))
li = sorted(li)
maximum = 0
for i in range(len(li)-2):
    for j in range(i+1, len(li)-1):
        if li[i] + li[j] <= li[j+1]:
            break
        for k in range(j+1, len(li)):
            if li[i] + li[j] <= li[k]:
                break
            maximum = max(maximum, li[i]+li[j]+li[k])
print(maximum)