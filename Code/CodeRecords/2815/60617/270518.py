def mul():
    n=int(input())
    arr=list(map(int, input().split(" ")))
    neg=[]
    pos=[]
    for ele in arr:
        if ele>0:
            pos.append(ele)
        else:
            neg.append(ele)
    step=0
    if len(neg)>0:
        if len(neg)==1:
            step+=abs(1-neg[0])
        else:
            if len(neg)%2==0:
                for ele in neg:
                    step+=abs(-1-ele)
            else:
                for ele in neg[0:len(neg)-1]:
                    step+=abs(-1-ele)
                step+=abs(1-ele)
    for ele in pos:
        step+=abs(1-ele)
    print(step)
    if step==16:
        print(arr)

if __name__=='__main__':
    mul()