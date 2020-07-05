import math
def binary(arr):
    res=0
    for i in range(0,len(arr)):
        res=res+int(math.pow(2,len(arr)-1-i))*arr[i]
    return res

t=input().split(',')
for i in range(0,len(t)):
    t[i]=int(t[i])
a=b=-1
for i in range(0,len(t)-2):
    for j in range(i+2,len(t)):
        if binary(t[0:i+1])==binary(t[i+1:j]) and binary(t[0:i+1])==binary(t[j:]):
            a=i
            b=j
            break
    if a!=-1:
        break
print('[' + str(a) + ', ' + str(b) + ']')
