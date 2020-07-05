x1_1,y1_1,x2_1,y2_1 = [int(i) for i in input().split(',')]
x1_2,y1_2,x2_2,y2_2 = [int(i) for i in input().split(',')]
x_in = (x1_2>min(x1_1,x2_1) and x1_2<=max(x1_1,x2_1)) or (x2_2>min(x1_1,x2_1) and x2_2<max(x1_1,x2_1))
y_in = (y1_2>min(y1_1,y2_1) and y1_2<=max(y1_1,y2_1)) or (y2_2>min(y1_1,y2_1) and y2_2<max(y1_1,y2_1))
if x_in and y_in:
    print("True")
else:
    print("False")