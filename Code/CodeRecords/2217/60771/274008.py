#26
from itertools import permutations

points = []
for i in range(0,4):
    ori = input().split(",")
    num = [int(item) for item in ori]
    points.append(num)
isValid = False
allPos = list(permutations(points,4))
# print(allPos)
for pointSet in allPos:
    A = pointSet[0]
    B = pointSet[1]
    C = pointSet[2]
    D = pointSet[3]
    
    AB = pow(A[0]-B[0],2) + pow(A[1]-B[1],2)
    BC = pow(C[0]-B[0],2) + pow(C[1]-B[1],2)
    CD = pow(C[0]-D[0],2) + pow(C[1]-D[1],2)
    DA = pow(A[0]-D[0],2) + pow(A[1]-D[1],2)
    # print("AB,BC,CD,DA: ",AB,BC,CD,DA)
    # 判断四条边是否相等+是否符合勾股定理
    if not (AB == BC and BC == CD and CD == DA and DA == AB):
        continue
    AC = pow(A[0]-C[0],2) + pow(A[1]-C[1],2)
    BD = pow(B[0]-D[0],2) + pow(B[1]-D[1],2)
    # print("AC and BD: ",AC,BD)
    if AC == BD:
        isValid = True
        break
    # 注意此处的边都是没开方的，所以不用平方，避免根号带来的偏差
    # if AB + BC == AC:
    #     isValid = True
    #     break
print(isValid)

