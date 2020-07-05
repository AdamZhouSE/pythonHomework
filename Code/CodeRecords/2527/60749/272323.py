str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
ans=str1.split("],[")
res=[]
for h in ans:
    res.append(list(map(int,h.split(","))))
vegan=int(input())
maxPrice=int(input())
maxDistance=int(input())
temp=[]
for t in res:
    if t[2]==vegan and t[3]<=maxPrice and t[4]<=maxDistance:
        temp.append(t)
temp=sorted(temp, key=lambda temp:(temp[1],temp[0]),reverse=True)
s=[]
for h in temp:
    s.append(h[0])
print(s)