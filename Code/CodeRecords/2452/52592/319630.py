n = int(input())

index = []
for i in range(n):
    n = eval(input())
    for i in n:
        index.append(i)
n = int(input())

f = "False"
for i in index:
    if(i == n):
        f = "True"
print(f)