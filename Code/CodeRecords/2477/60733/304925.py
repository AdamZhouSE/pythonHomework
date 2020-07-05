t = int(input())
for m in range(t):
    line = list(map(int, input().split()))
    R1_LTx = line[0]
    R1_LTy = line[1]
    R1_RBx = line[2]
    R1_RBy = line[3]
    line = list(map(int, input().split()))
    R2_LTx = line[0]
    R2_LTy = line[1]
    R2_RBx = line[2]
    R2_RBy = line[3]
    if R1_RBy > R2_LTy or R2_RBy > R1_LTy:
        print(0)
    elif R1_LTx > R2_RBx or R2_LTx > R1_RBx:
        print(0)
    else:
        print(1)