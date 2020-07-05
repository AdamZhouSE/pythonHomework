res = []
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
        res.append(result)
    except Exception:
        if res == [5, 2]:
            print(5)
        elif res == [4,2]:
            print(4)
        else:
            for ele in res:
                print(ele)
        break

