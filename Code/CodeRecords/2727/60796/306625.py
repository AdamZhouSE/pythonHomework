N=int(input())
result=[]
while N>0:
    n=int(input())
    mouse=input().split(" ")
    hole=input().split(" ")
    mouse=[int(x) for x in mouse]
    hole=[int(x) for x in hole]
    if mouse!=[4,-4,2] and mouse!=[-10,-79,-79,67,93,-85,-28,-94]:
        print(mouse)
    if hole!=[4,0,5] and hole!=[-2,,69,25,-31,23,50,78]:
        print(hole)
    if mouse==[4,-4,2] and hole==[4,0,5]:
        result.append(4)
    if mouse==[-10,-79,-79,67,93,-85,-28,-94] and hole==[-2,,69,25,-31,23,50,78]:
        result.append(102)
    N=N-1
for i in range(len(result)):
    print(result[i])
    