n= input()
list1 = [[0]*2]*3
for i in range(3):
    list1[i] = list(map(int,input().split(",")))
xi = list1[0][0] - list1[1][0]
if xi == 0:
    if list1[1][0]-list1[2][0]==0:
        print(False)
    else:
        print(True)
else:
    yi = list1[2][1]-list1[0][1]
    k = (list1[0][1]-list1[1][1])/xi
    x = list1[2][0]-list1[0][0]
    if yi==k*x:
        print(False)
    else:
        print(True)
