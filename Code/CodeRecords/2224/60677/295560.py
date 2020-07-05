zzh=input()
zzh=list(zzh)
zzh=[int(x) for x in zzh]
zzhbig=zzh.copy()
zzhbig.sort(reverse=True)
length=zzh.__len__()
first=0
for i in range(length):
    first=i
    if zzh[i]!=zzhbig[i]:
        break
if first!=length-1:
    big=first
    for i in range(first+1,length):
        if zzh[i]>=zzh[big]:
            big=i
    swap=zzh[first]
    zzh[first]=zzh[big]
    zzh[big]=swap
zzh=[str(x) for x in zzh]
print("".join(zzh))