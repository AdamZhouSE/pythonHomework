rectangle_nums=(int)(input())
rectangles=[]
for i in range(rectangle_nums):
    rectangles.append(list(map(int,input().split(' '))))
judge='YES'
rectangles[0]=max(rectangles[0])
for i in range(1,len(rectangles)):
    if(rectangles[i-1]<min(rectangles[i])):
        judge='NO'
        break
    elif(max(rectangles[i])<rectangles[i-1]):
        rectangles[i]=max(rectangles[i])
    else:
        rectangles[i]=min(rectangles[i])
print(judge)