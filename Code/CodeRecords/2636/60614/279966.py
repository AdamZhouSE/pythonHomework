def findRoute(roads,first,second,route,sum):
    if first==second:
        route.append(first)
        return [route,sum]
    elif first in route:
        return -1
    else:
        route.append(first)
        result=[[],100]
        for i in roads:
            if i[0]==first:
                temp=findRoute(roads,i[1],second,route,sum+i[2])
                if temp!=-1:
                    if temp[1]<result[1]:
                        result=temp
            elif i[1]==first:
                temp=findRoute(roads,i[0],second,route,sum+i[2])
                if temp!=-1:
                    if temp[1]<result[1]:
                        result=temp
        return result
init=[int(x) for x in input().split()]
roads=[]
for i in range(init[1]):
    roads.append([int(x) for x in input().split()])
max=[[],0]
for i in range(init[0]):
    for j in range(init[0]):
        temp=findRoute(roads,i+1,j+1,[],0)
        if temp[1]>max[1] and temp[1]!=100:
            max=temp
print(int(max[1]/2)+max[1])