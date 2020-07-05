import itertools
def func(list1):
    ma=max(list1)
    return (sum(list1)-ma)<=ma
num=input().split(",")
num=list(map(int,num))
list2=itertools.combinations(num,3)
c=[]
for list1 in list2:
    if(func(list1)):
        c.append(0)
    else:
        c.append(sum(list1))
print(max(c))
