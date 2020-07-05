size=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(size)]
list1.insert(0,0)
base=0
count=0
for i in range(size):
    base+=(list1[i]-list1[i+1])
    if base<0:
        count+=abs(base)
        base=0
print(count)