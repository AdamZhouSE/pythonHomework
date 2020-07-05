def dance():
    n=int(input())
    a=list(map(int, input().split(" ")))
    m=int(input())
    b=list(map(int, input().split(" ")))
    boys=a.copy()
    girls=b.copy()
    pairs=0
    boys.sort()
    girls.sort()
    if n<=m:
        for ele in boys:
            if ele-1 in girls:
                pairs+=1
                girls.remove(ele-1)
            elif ele in girls:
                pairs+=1
                girls.remove(ele)
            elif ele+1 in girls:
                pairs+=1
                girls.remove(ele+1)

    else:
        for ele in girls:
            if ele-1 in boys:
                pairs+=1
                boys.remove(ele-1)
            elif ele in boys:
                pairs+=1
                boys.remove(ele)
            elif ele+1 in girls:
                pairs+=1
                boys.remove(ele+1)
    if pairs==6:
        print(boys)
        print(girls)
        print(a)
        print(b)
        print(len(a))
        print(len(b))
    print(pairs)

if __name__=='__main__':
    dance()