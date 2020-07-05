n=int(input())
points=[]
c=0
for i in range(n):
    s=""
    list2=[]
    s=input().split(",")
    a=int(s[0])
    b=int(s[1])
    list2.append(a)
    list2.append(b)
    points.append(list2)

for i in range(len(points)-1):
            c+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))

print(c)