n = int(input())
x = 0
a = []
while(x < n):
    a.append([int(i) for i in input().split(',')])
    x+=1
if(n==1):
    print(True)
else:
    result = True
    offset_x = a[1][0] - a[0][0]
    offset_y = a[1][1] - a[0][1]
    for i in range(1,n-1):
        if(offset_x == 0):
            if(a[i+1][1]!=a[i][1]):
                result = False
                break
        elif(offset_y==0):
            if(a[i+1][0]!=a[i][0]):
                result = False
                break
        else:    
            if((a[i+1][0]-a[i][0])/offset_x != (a[i+1][1]-a[i][1])/offset_y):
                result = False
                break
    print(result)
            