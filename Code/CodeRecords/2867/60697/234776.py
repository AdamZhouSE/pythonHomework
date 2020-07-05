array=[]
for i in range(5):
    array.append(list(map(int,input().split(' '))))

for i in range(5):
    for j in range(5):
        if(array[i][j]==1):
            x=i
            y=j
            break
print(abs(x-2)+abs(y-2))