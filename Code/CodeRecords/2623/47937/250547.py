x=eval(input())
y=int(input())
result=[]
i=0
while i<len(x):
    result.append(int(x[i]))
    i=i+1

result.sort()

print(result[len(result)-y])