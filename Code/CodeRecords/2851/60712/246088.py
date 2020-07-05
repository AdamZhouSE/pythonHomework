n= int(input())
list1=[[]*2]*n
maxX= 0
maxY= 0
maxl=0
for i in range(n):
    list1[i] = list(map(int,input().split()))
for i in range(n):
    if list1[i][0]>=maxl or list1[i][1]>=maxl:
        maxX=list1[i][0]
        maxY=list1[i][1]
        maxl= list1[i][0] if list1[i][0]>=list1[i][1] else list1[i][1]
b = maxY+maxX
print(b)
