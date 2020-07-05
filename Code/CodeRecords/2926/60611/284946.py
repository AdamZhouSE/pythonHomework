l=[]
l.append(int(input()))
l.append(list(map(int,input().split(" "))))
s=set(l[1])
length=0
for i in s:
    if length<l[1].count(i):
        length=l[1].count(i)
print(length)