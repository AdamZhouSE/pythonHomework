x=int(input())
y=int(input())
bound=int(input())
a=0
i_max,j_max=0,0
re=[]
while x**a<bound or y**a<bound:
    if x**a<bound:
        i_max=a
    if y**a<bound:
        j_max=a
    a+=1
for i in range(0,i_max+1):
    for j in range(0,j_max+1):
        if x**i+y**j<=bound:
            re.append(x**i+y**j)
print(sorted(list(set(re))))