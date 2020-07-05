def colornum(colors):
    ans=0
    for color in colors:
        if colors.count(color)>=2:
            ans+=1
            while color in colors:
                colors.remove(color)
    return ans
    

n,c,m=map(int,input().split())
colors=list(map(int,input().split()))
for i in range(m):
    start,end=map(int,input().split())
    print(colornum(colors[start-1:end]))