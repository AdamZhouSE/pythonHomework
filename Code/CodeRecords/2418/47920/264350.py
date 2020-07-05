ts = int(input())
cs = int(input())
#print(ts)
#print(cs)
result = []

x = (ts-2*cs)/2
y = (4*cs-ts)/2
if(x >= 0 and y >= 0):
    result.append(int(x))
    result.append(int(y))
print(result)