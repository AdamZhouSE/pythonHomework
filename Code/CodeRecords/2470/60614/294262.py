for i in range(int(input())):
    length=int(input())
    init=[int(x) for x in input().split()]
    matrix=[]
    for j in range(length):
        for k in range(length-1,-1,-1):
            matrix.append(str(init[k*length+j]))
    print(" ".join(matrix))