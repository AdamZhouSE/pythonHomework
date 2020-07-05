temp=input().split(" ")
n=int(temp[0])
d=int(temp[1])
res=[]

number=int(input())
for i in range(number):
    pos=input().split(" ")
    x=int(pos[0])
    y=int(pos[1])

    if d<n/2:
        if x<d and x>=0:
            if y<=x+d and y>=-x+d:
                res.append("YES")
            else:
                res.append("NO")
        elif x<n-d:
            if y<=x+d and y>=x-d:
                res.append("YES")
            else:
                res.append("NO")
        elif x<=n:
            if y<=-x+2*n-d and y>=x-d:
                res.append("YES")
            else:
                res.append("NO")
        else:
            res.append("NO")
    else:
        if x<n-d and x>=0:
            if y<=x+d and y>=-x+d:
                res.append("YES")
            else:
                res.append("NO")
        elif x<d:
            if y<=-x+2*n-d and y>=-x+d:
                res.append("YES")
            else:
                res.append("NO")
        elif x<=n:
            if y<=-x+2*n-d and y>=x-d:
                res.append("YES")
            else:
                res.append("NO")
        else:
            res.append("NO")
            
for i in res:
    print(i)