n,k=map(int,input().split())
square=[]
for i in range(0,n):
    square.append([int(t) for t in input().split()])
re=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if abs(square[i][0]-square[j][0])<k and abs(square[i][1]-square[j][1])<k and re==0:
            re=(k-abs(square[i][0]-square[j][0]))*(k-abs(square[i][1]-square[j][1]))
        elif abs(square[i][0]-square[j][0])<k and abs(square[i][1]-square[j][1])<k and (not re==0):
            re=-1
            break
    else:
        continue
    break
print(re)