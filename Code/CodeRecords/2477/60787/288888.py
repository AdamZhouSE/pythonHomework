t=int(input())

def isIn(point,tri):
    if point[0]>=tri[0] and point[0]<=tri[2] and point[1]>=tri[3] and point[1]<=tri[1]:
        return True
    else:
        return False

for ex in range(0,t):
    a=[int(i) for i in input().split(" ")]
    b=[int(i) for i in input().split(" ")]
    if isIn([a[0],a[1]],b) or isIn([a[0],a[3]],b) or isIn([a[2],a[1]],b) or isIn([a[2],a[3]],b):
        print(1)
    else:
        print(0)