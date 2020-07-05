n=int(input())
x=[]
y=[]
for _ in range(n):
    temp=[int(x) for x in input().split(" ")]
    x.append(temp[0])
    y.append(temp[1])
print(min(len(set(x))-1,len(set(y))-1))