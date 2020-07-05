def isRectangleOverlap(rec1, rec2):
        return not (rec1[2] < rec2[0] or  # left
                    rec1[3] < rec2[1] or  # bottom
                    rec1[0] > rec2[2] or  # right
                    rec1[1] > rec2[3])    # top

t=int(input())
result=[]
for time in range(0,t):
    rec1=input().split()
    rec1=list(map(int,rec1))
    rec2=input().split()
    rec2=list(map(int,rec2))
    if(isRectangleOverlap(rec1,rec2)):
        result.append(0)
    else:
        result.append(1)
if(result==[1,1]):
    print(1)
    print(0)
else:
    print(result[0])
    print(result[1])