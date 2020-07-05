cnt=int(input())
coordinates=[]
for i in range(0,cnt):
    temp=input()
    temp=list(map(int,temp.split(',')))
    coordinates.append(temp)
ans = []
for i in range(1, len(coordinates)):
    if coordinates[i][0] - coordinates[i-1][0] == 0:
        k = float("inf")
    else:
        k = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
    ans.append(k)
print(len(set(ans)) == 1)