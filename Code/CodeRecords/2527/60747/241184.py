import re
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
restaurants=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        restaurants.append(new)
        a=0
        new=[]
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
restaurants.sort(key=lambda x: (-x[1], -x[0]))
print([i for i, _, v, p, d in restaurants if v >= veganFriendly and p <= maxPrice and d <= maxDistance])