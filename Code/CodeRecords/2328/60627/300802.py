a = eval(input())
max = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for m in range(4):
                if(a[i]*10 + a[j]<24 and a[k]*10 + a[m]<60):
                    max.append((a[i]*10 + a[j])*60 + a[k]*10 + a[m])
print(max(max))
    