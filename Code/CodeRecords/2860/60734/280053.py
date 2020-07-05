n = int(input())
x = []
y = []

for i in range(n):
    lst = list(map(int,input().split(' ')))
    x.append(lst[0])
    y.append(lst[1])
    
print(min(len(set(x)),len(set(y)))-1)