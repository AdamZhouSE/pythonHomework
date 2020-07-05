a=eval(input())
k=int(input())
r=[]
cal=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        r.append([a[i],a[j]])
        cal.append(a[i]/a[j])
re=sorted(cal)
index=cal.index(re[k-1])
print(r[index])