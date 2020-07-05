a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

my_set=set([])
for x in l:
    my_set.add(x)

res=1
while my_set.__contains__(res):
    res++
print(res)