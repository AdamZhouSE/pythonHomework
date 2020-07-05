def canReturn(degrees,nowDegree):
    if len(degrees)==0:
        if nowDegree%360 == 0:
            return True
        else:
            return False
    else:
        degree = degrees.pop(0)
        return canReturn(degrees.copy(),nowDegree+degree) or canReturn(degrees.copy(),nowDegree-degree)
    
numOfInput = int(input())
degrees = []
for i in range(numOfInput):
    degree = int(input())
    degrees.append(degree)
if canReturn(degrees,0):
    print("YES")
else:
    print("NO")