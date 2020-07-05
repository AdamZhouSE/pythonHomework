a=int(input())
list=[]
for i in range(a):
    list.append(input())
maximum=0
for i in range(a):
    maximum=max(maximum,list.count(list[i]))
print(maximum)