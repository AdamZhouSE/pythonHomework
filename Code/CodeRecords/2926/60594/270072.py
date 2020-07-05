n=int(input())
row=[int(n) for n in input().split()]
kd=[[row[0]]]
for index in range(1,n):
    jishu=0
    for j in kd:
        cunzai=False
        for k in j:
            if k==row[index]:
                cunzai=True
                break
        if not cunzai:
            j.append(row[index])
            break
        jishu+=1
    if jishu==len(kd):
        kd.append([row[index]])
print(len(kd))

