data = list(map(int,input().split(',')))
max = data[0]
for i in range(0,len(data)):
    for j in range(len(data),i,-1):
        result = sum(data[i:j])
        if(result > max):
            max = result
    result = sum(data[i:])
    if(result > max):
        max = result
print(max)