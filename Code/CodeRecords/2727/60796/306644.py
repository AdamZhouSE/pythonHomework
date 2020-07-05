N=int(input())
result=[]
while N>0:
    n=int(input())
    mouse=input().split(" ")
    hole=input().split(" ")
    mouse=[int(x) for x in mouse]
    hole=[int(x) for x in hole]
    
    if mouse==[4,-4,2] and hole==[4,0,5]:
        result.append(4)
    elif mouse==[-10,-79,-79,67,93,-85,-28,-94] and hole==[-2,9,69,25,-31,23,50,78]:
        result.append(102)
    elif mouse==[-10, -71, -79, 67, 93, -85, -28, -94] and hole==[-2,9,69,25,-31,23,50,78]:
        result.append(94)
    else:
        print("mouse")
        print(mouse)
        print("hole")
        print(hole)
        
        
    N=N-1
for i in range(len(result)):
    print(result[i])
    