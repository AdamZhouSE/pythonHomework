n=input();
d=[None for _ in range(10)]
for i,digit in enumerate(n):
    d[int(digit)]=i
res=n
jflag=False
for i,digit in enumerate(n):
    for index in range(9,int(digit),-1):
        if d[index]!= None and d[index] > i:
            res=n[: i] + n[d[index]] + n[i + 1: d[index]] + n[i] + n[d[index] + 1:]
            jflag=True
            break
    if(jflag):break
print(res)