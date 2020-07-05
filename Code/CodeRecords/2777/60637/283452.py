tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    scores=list(map(int,input().split(' ')))
    list.sort(scores)
    if(n%2==0):
        print((int)((scores[(int)(n/2)-1]+scores[(int)(n/2)])/2))
    else:
        print(scores[(int)(n/2)])
