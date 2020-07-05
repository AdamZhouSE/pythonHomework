n=bin(int(input()))[2:]
res=0
rec=-1
for i in range(len(n)):
    if n[i]=='1' and rec!=-1:
        res=max(res,i-rec)
        rec=i
    elif n[i]=='1':
        rec=i
print(res)
