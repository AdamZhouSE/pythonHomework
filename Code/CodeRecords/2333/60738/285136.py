x=int(input())
y=int(input())
bound=int(input())
num_list=[]
for  i in range(bound):
    for j in range(bound):
        if ((x**i+y**j)<=bound):
            c=x**i+y**j
            if num_list.count(c)<1:
                num_list.append(c)
num_list.sort()
print(num_list)