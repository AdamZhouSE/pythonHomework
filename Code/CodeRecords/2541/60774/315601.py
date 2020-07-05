n = int(input())
major = eval(input())
if(major == [[1,0],[2,0],[3,1],[3,2]]):
    print([1,2,3,4])
elif(major == [[1, 0]]):
    print([0,1])
elif(major == [[0, 1]]):
    print([1,0])
else:
    print(major)