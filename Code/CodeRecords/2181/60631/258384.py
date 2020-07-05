data=[]
n = int(input())
for i in range(1000):
    data.append(i**3+i)
for j in range(n):
    print(data[int(input())])