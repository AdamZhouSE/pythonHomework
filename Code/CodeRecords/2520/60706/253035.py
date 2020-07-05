def allCellsDistOrder( R, C, r0, c0):
        return sorted([[i, j] for i in range(R) for j in range(C)], key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
list=allCellsDistOrder(R,C,r0,c0)
print(list)
