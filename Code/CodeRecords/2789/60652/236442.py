def side_len():
    n=int(input())
    arr=list(map(int,input().split(" ")))
    arr.sort(reverse=True)
    sl=0
    for i in arr:
        if sl<i:
            sl+=1
        else:
            break
    return sl


k=int(input())
for i in range(0,k):
    print(side_len())
