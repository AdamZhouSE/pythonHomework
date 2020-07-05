a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

res=1

my_set=set([])
for x in l:
    my_set.add(x)

for x in my_set:
    if x-1 not in my_set:
        curr=x
        while curr+1 in my_set:
            curr+=1
        res=max(curr-x+1,res)

print(res)