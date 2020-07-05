k = int(input())
n = int(input())
index = 0
while True:
    if 2**index<n and 2**(index+1)>=n:
        break
    index+=1
print(index)