stra = input().split(',')
strb = input().split(',')
rec1 = [int(i) for i in stra]
rec2 = [int(i) for i in strb]
check = not (rec1[2]<rec2[0] or rec1[3]<rec2[1]) or (rec1[0]>rec2[2] or rec1[1]>rec2[3])
print(check)