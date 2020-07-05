a=list(map(int,input().replace(']','').replace('[','').split(',')))
cnt=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>2*a[j]:
            cnt+=1
print(cnt)            