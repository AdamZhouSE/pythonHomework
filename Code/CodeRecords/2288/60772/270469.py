while True:
    try:
        i,num = list(map(int,input().split()))
        result,level = 1,1
        leftNode,rightNode = 2*i,2*i+1
        while rightNode <= num:
            level *= 2
            result += level
            leftNode *= 2
            rightNode = rightNode*2 + 1
        if leftNode <= num:
            result += num-leftNode+1
        print(result)
    except Exception:
        break
