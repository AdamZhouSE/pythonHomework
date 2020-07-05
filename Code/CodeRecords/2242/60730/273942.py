rec1 = eval(input())
rec2 = eval(input())
tmp_1 = rec1[2:]
tmp_2 = rec2[:2]
tmp_3 = rec1[:2]
tmp_4 = rec2[2:]
if (tmp_1[1] > tmp_2[1] and tmp_1[0] > tmp_2[0]) or (tmp_4[1] > tmp_3[1] and tmp_4[0] > tmp_3[0]):
    print("True")
else:
    print("False")
