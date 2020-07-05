a=input()
b=eval(input())
start=0
end=0
d={}
d[a[0]]=1
length=end-start+1
while end<len(a):
    maxmum=0
    for i in d.keys():
        maxmum=max(maxmum,d[i])
    if(maxmum+b)>=(end-start+1):
        length = max(length, end-start+1)
        end+=1
        if(end<len(a)):
            if(a[end] in d ):
                d[a[end]]=d[a[end]]+1
            else:
                d[a[end]]=1
        else:
            break
    else:
        start+=1
        d[a[start]]=max(0,d[a[start]]-1)

print(length)
