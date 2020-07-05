def area(a,b,c):
    x=(a[0]-b[0],a[1]-b[1])
    y=(a[0]-c[0],a[1]-c[1])
    return abs(x[0]*y[1]-x[1]*y[0])/2.0

def maxArea(alist):
    max = 0.0
    n=len(alist)
    alist=list(set(alist))
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(max<area(alist[i],alist[j],alist[k])):
                    max = area(alist[i],alist[j],alist[k])
    return max


n=int(input())
alist = []
for i in range(n):
    location = tuple(map(int,input().split(',')))
    alist.append(location)
print(maxArea(alist))





