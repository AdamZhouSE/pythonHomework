13
25
27
n = int(input())
data=[]
for i in range(1,500):
    data.append(i*(2*i+1))
for j in range(n):
    m=int(input())
    print(data[m-1])