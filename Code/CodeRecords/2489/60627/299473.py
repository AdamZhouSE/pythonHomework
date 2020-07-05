l = eval(input())
a = int(input())
b = int(input())
i=0
for i in range(len(l)):
    for j in range(i,len(l)):
        print(i,j)
        if a<=sum(l[i:j+1])<=b and i!=j:
            i += 1
print(i)