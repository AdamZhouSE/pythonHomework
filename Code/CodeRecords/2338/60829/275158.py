def x(a,p):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==p:
                return "Yes"
    return "No"
n=int(input())
for i in range(n):
    n=[int(x) for x in str(input()).split(" ")]
    a=[int(x) for x in str(input()).split(" ")]
    print(x(a,n[1]))