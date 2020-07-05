def input_manage():
    destination=int(input())
    start=input()
    speed=input()
    start=start[1:len(start)-1]
    start=start.split(',')
    speed=speed[1:len(speed)-1]
    speed=speed.split(',')
    array=[[0 for _ in range(3)] for _ in range(len(start))]
    for i in range(len(start)):
        array[i][0]=(destination-int(start[i]))/int(speed[i])
        array[i][1]=int(start[i])
        array[i][2]=int(speed[i])
    array.sort()
    return array
array=input_manage()
count=len(array)
for i in range(len(array)-1):
    if array[i][1]<=array[i+1][1]:
        count=count-1
print(count)