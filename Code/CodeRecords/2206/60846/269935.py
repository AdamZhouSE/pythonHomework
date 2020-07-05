t=int(input())
list=[]
line=[]
while t:
    line.append(int(input()))
    t-=1
max=max(line)
for i in range(max):
    start=1+i*(i+1)//2
    product=1
    for j in range(i+1):
        product*=(start+j)
    list.append(product)
for i in range(len(line)):
    output=0
    for j in range(line[i]):
        output+=list[j]
    print(output)