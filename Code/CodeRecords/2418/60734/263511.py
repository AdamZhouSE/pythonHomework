t = int(input())
c = int(input())
'''
设制作x个巨无霸 y个小皇堡 
    4x+2y = t
    x+y = c
解得 x = t/2 - c
     y = 2c - t/2
'''
if t%2 == 0:
    x = t/2 - c
    y = 2*c - t/2
    if x>=0 and y>=0:
        print([x,y])
print([])