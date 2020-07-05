t = int(input())
c = int(input())

result = []
l1=t-2*c
l2=4*c-t
x = (t-2*c)/2
y = (4*c-t)/2
if(x >= 0 and y >= 0):
    a=int(x)
    b=int(x)
    result.append(int(x))
    result.append(int(y))
print(result)