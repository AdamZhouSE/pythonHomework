x=int(input())
y=int(input())
bound=int(input())
result=set()
for i in range(20):
    for j in range(20):
        if x**i + y**j <= bound:
            result.add(x**i + y**j)
print(list(result))