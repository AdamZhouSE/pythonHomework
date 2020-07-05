rec1=list(eval(input()))
rec2=list(eval(input()))
if rec2[2]<=rec1[0] or rec2[0]>=rec1[2] or rec2[3]<=rec1[1] or rec2[1]>=rec1[3]:
    print('False')
else:
    print('True')