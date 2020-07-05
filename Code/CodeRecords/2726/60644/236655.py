arr=input()[1:-1].split(',')

for i in range(0,len(arr)):
    if arr[i]=='null' and arr[i+1]=='null' and i%2!=0:
        x=i+1
        break
depth=0
while x>=2:
    x=x/2
    depth=depth+1
print(depth)