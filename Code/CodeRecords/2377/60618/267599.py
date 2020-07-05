xy=eval(input())
k=(xy[0][1]-xy[1][1])//(xy[0][0]-xy[1][0])
re=1
for i in range(1,n):
    if (xy[i][1]-xy[0][1])//(xy[i][0]-xy[0][0])==k:
        re=0
if re==1:
    print("True")
else:
    print("False")