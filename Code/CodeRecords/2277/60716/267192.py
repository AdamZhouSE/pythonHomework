k = int(input())
n = int(input())
#print(n)
index = 0
while index<n:
    if 2**index<=n and 2**(index+1)>n:
        break
    index+=1
print(index)