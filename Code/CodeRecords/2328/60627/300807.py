a = eval(input())
ma = 0
s = ''
for i in range(4):
    for j in range(4):
        for k in range(4):
            for m in range(4):
                if(a[i]*10 + a[j]<24 and a[k]*10 + a[m]<60 and i!=j and i!=k and i!=m and j!=k and j!=m and k!=m ):
                    if (a[i]*10 + a[j])*60 + a[k]*10 + a[m]>ma:
                        ma = (a[i]*10 + a[j])*60 + a[k]*10 + a[m]
                        s = str(a[i]) + str(a[j]) + ':' + str(a[k]) + str(a[m])
print(s)
