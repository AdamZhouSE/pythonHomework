def find_destination(array,place):
    ans=-1
    for i in range(len(array)):
        if array[i][0]==place:
            ans=i
            break
    return ans
plane=eval(input())
plane.sort()
start="JFK"
result=["JFK"]
count=find_destination(plane,start)
while count!=-1:
    start=plane[count][1]
    plane.pop(count)
    result.append(start)
    count=find_destination(plane,start)
print(result)