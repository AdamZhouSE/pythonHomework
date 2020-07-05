points = eval(input())
k = int(input())
points.sort(key=lambda x:x[0]**2+x[1]**2)
print([points[i] for i in range(k)])