n=int(input(""))
points=[]
moves=0
for i in range(n):
    points.append(input(""))
for i in range(1,n):
    num1=points[i][0]-points[i-1][0]
    num2=points[i][1]-points[i-1][1]
    moves=moves+max(abs(num1),abs(num2))
print(moves)            