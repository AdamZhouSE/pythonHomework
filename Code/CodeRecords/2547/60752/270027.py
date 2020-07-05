for b in range(int(input())):
    size=int(input())
    ele=list(map(int,input().split()))
    k=int(input())
    count=0
    existed=[]
    for aa in range(size-1):
        for bb in range(aa+1,size):
            ab=[ele[aa],ele[bb]]
            ab.sort()
            if abs(ele[aa]-ele[bb])==k and existed.count(ab)==0:
                count+=1
                existed.append(ab)
    print(count)






