s=input()
ans=''
dic={}
for x in s:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1

temp=list(dic.items())

temp=[[x,y] for (y,x) in temp]

temp.sort(reverse=True)

for (v,k) in temp:
    for i in range(0,v):
        print(k,end='')
print()
