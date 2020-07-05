def solve():
    total=int(input())
    rectangles=[]
    for i in range(total):
        rectangles.append(list(map(int,input().split())))
    last=max(rectangles[0])
    if total<=1:
        print("YES")
        return 
    for i in range(total):
        if min(rectangles[i])>last:
            print("NO")
            return
        if max(rectangles[i])<=last:
            rectangles[i].sort()
        else:
            rectangles[i].sort(reverse=True)
        last=rectangles[i][1]

    print("YES")

if  __name__ == '__main__' :
    solve()
