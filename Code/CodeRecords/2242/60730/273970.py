rec1 = eval(input())
rec2 = eval(input())

if rec1[2]<=rec2[0] or rec1[3]<=rec2[1] or rec1[0]>=rec2[2] or rec1[1]>=rec2[3]:  # 两矩形不接触的情况
    print("False")
else:
    print("True")
