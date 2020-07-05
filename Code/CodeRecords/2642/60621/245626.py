a=[int(x) for x in input().split(",")]
a.sort()
maxmum=a[len(a)-1]-a[0]+1-len(a)-min(a[len(a)-1]-a[len(a)-2]-1,a[1]-a[0]-1)
start=0
end=0
minmum=0
now=0
while end<len(a):
    flag = 0
    if(a[end]-a[start]+1<=len(a)):
        if(a[end]-a[start]+1-len(a)==-1):
            flag=1
        now+=1
        end+=1
    else:
        now-=1
        start+=1

    minmum=max(minmum,now-flag)

minmum=len(a)-minmum

print([minmum,maxmum])