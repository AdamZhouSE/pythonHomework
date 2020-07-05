def solve():
    t=int(input())
    c=int(input())
    x=(t-2*c)/2
    y=(4*c-t)/2
    ix,iy=int(x),int(y)
    res=[ix,iy]
    if x-ix==0 and y-iy==0 and iy>=0 and ix>=0:
        print(res)
    else:
        print([])

if  __name__ == '__main__' :
    solve()