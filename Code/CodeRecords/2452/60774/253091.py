n = int(input())
matrix = []
for i in range(0,n):
    temp = list(map(int,input().split(',')))
    matrix.append(temp)
target = int(input())
flag = False
for i in range(0,len(matrix)):
    if(matrix[i][0] > target and i != 0):
        pro = matrix[i - 1]
        for n in pro:
            if(n == target):
                flag = True
                print(flag)
                break
        break
if(not flag):
    print(flag)