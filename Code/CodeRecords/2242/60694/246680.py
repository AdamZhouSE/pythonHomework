rec1 = list(map(int, input().split(",")))
rec2 = list(map(int, input().split(",")))
# 以rec1为基准 上左右下条件
if rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3]:
    print("False")
else:
    print("True")
