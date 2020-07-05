x=int(input())
y=int(input())
bound=int(input())
result=[]
def f(n):
    for i in range(bound):
        for j in range(bound):
            if(n==x**i+y**j):
                return True
    return False
for i in range(1,bound+1):
    if(f(i)):
        result.append(i)
print(result)