def vertexjudge(rectangle1,rectangle2):
    bool = [False,False,False,False]
    # 左下角在内部\右下角在内部\右上角在内部\左上角在内部
    if int(rectangle1[0][0]) < int(rectangle2[0][0]) < int(rectangle1[2][0]) and int(rectangle1[0][1]) < int(rectangle2[0][1]) < int(rectangle1[2][1]):
        bool[0]=True
    elif int(rectangle1[0][0]) < int(rectangle2[1][0]) < int(rectangle1[2][0]) and int(rectangle1[0][1]) < int(rectangle2[1][1]) < int(rectangle1[2][1]):
        bool[1]=True
    elif int(rectangle1[0][0]) < int(rectangle2[2][0]) < int(rectangle1[2][0]) and int(rectangle1[0][1]) < int(rectangle2[2][1]) < int(rectangle1[2][1]):
        bool[2]=True
    elif int(rectangle1[0][0]) < int(rectangle2[3][0]) < int(rectangle1[2][0]) and int(rectangle1[0][1]) < int(rectangle2[3][1]) < int(rectangle1[2][1]):
        bool[3]=True
    return bool


def calculatearea(vertex1,vertex2):
    area = abs(int(vertex2[0])-int(vertex1[0]))*abs(int(vertex2[1])-int(vertex1[1]))
    return area


source = input().split(',')
rectangle1 = []
rectangle2 = []
sum = 0
rectangle1.append([source[0],source[1]])
rectangle1.append([source[2],source[1]])
rectangle1.append([source[2],source[3]])
rectangle1.append([source[0],source[3]])
rectangle2.append([source[4],source[5]])
rectangle2.append([source[6],source[5]])
rectangle2.append([source[6],source[7]])
rectangle2.append([source[4],source[7]])
area1 = calculatearea(rectangle1[0],rectangle1[2])
area2 = calculatearea(rectangle2[0],rectangle2[2])
map = vertexjudge(rectangle1,rectangle2)

same = 0
if map.count(True)==1:
    index = map.index(True)
    if index==0 or index==1:
        same = calculatearea(rectangle2[index],rectangle1[index+2])
    elif index==2 or index==3:
        same = calculatearea(rectangle1[index-2],rectangle2[index])
elif map.count(True)==2:
    if map[0]==True and map[1]==True:
        same = abs(int(rectangle2[1][0])-int(rectangle2[0][0]))*abs(int(rectangle1[2][1])-int(rectangle2[0][1]))
    elif map[1]==True and map[2]==True:
        same = abs(int(rectangle1[0][0]) - int(rectangle2[1][0])) * abs(int(rectangle2[2][1]) - int(rectangle2[1][1]))
    elif map[2]==True and map[3]==True:
        same = abs(int(rectangle2[1][0]) - int(rectangle2[0][0])) * abs(int(rectangle1[0][1]) - int(rectangle2[3][1]))
    elif map[3]==True and map[0]==True:
        same = abs(int(rectangle2[0][0]) - int(rectangle1[1][0])) * abs(int(rectangle2[2][1]) - int(rectangle2[1][1]))
elif map.count(True)==4:
    same = area2
sum = area1+area2-same
print(sum)



