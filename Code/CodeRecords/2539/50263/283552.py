n = eval(input())
m = []
for i in range(0,len(n)):
    for j in range(i,len(n)):
        for k in range(i+1):
            if n[i]>n[j] or n[i]<n[k]:
                m.append(i)
                break
print(max(m)-min(m)+1)
