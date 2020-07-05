seq=input()
res=[0]*len(seq)
for i in range(1,len(seq)):
    if seq[i]==seq[i-1]:
        res[i]=1-res[i-1]
    else:
        res[i]=res[i-1]
print(res)
