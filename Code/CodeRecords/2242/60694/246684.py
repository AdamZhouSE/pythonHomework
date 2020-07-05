rec1 = list(map(int, input().split(",")))
rec2 = list(map(int, input().split(",")))
# 以rec1为基准 分列rec2在rec1的 上/左/右/下 方的条件，此为false
if rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3]:
    print("False")
else:
    print("True")
