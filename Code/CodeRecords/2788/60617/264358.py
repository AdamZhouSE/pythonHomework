def dance():
    n=int(input())
    boys=list(map(int, input().split(" ")))
    m=int(input())
    girls=list(map(int, input().split(" ")))
    pairs=0
    boys.sort()
    girls.sort()
    if n<=m:
        for ele in boys:
            if ele+1 in girls:
                pairs+=1
                girls.remove(ele+1)
            elif ele-1 in girls:
                pairs+=1
                girls.remove(ele-1)
    else:
        for ele in girls:
            if ele+1 in boys:
                pairs+=1
                boys.remove(ele+1)
            elif ele-1 in girls:
                pairs+=1
                boys.remove(ele-1)
    print(pairs)
    
if __name__=='__main__':
    dance()