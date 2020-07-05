s=list(map(int,input().split(' ')))
n=s[0]
k=s[1]
names=[]
for i in range(n):
    s=list(input().split())
    if(int(s[1])==0):
        names.append(s[0])
        continue
    names.append(s[0]+names[int(s[1])-1])

for i in range(k):
    tmp=input()
    count=0
    for z in names:
        if z.startswith(tmp):count+=1
    print(count)


