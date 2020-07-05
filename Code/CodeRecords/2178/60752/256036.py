size=int(input())
lst=list(map(int,input().split(' ')))
for l in range(1,size+1):
    has=[]
    magic=lst[0:l+1]
    for length in range(1,l+1):
        for start in range(0,l-length+1):
            if has.count(magic[start:start+length])==0:
                has.append(magic[start:start+length])
    print(len(has))


