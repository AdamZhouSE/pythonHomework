from itertools import combinations
def largestTriangleArea(points):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
points=[]
i=0
while i<len(list1)-1:
    list2=[]
    list2.append(int(list1[i]))
    list2.append(int(list1[i+1]))
    points.append(list2)
    i=i+2
ans=largestTriangleArea(points)
print(ans)