for b in range(int(input())):
    s=input()
    k=int(input())
    chrs=[]
    rs=''
    start=0
    length=len(s)
    found=False
    while not found:
        while start<len(s)-length:
            chrs.clear()
            ss=s[start:start+length+1]
            for sss in ss:
                if chrs.count(sss)==0:chrs.append(sss)
            start+=1
            if len(chrs)==k:
                rs=ss
                found=True
                break
        length-=1
    print(len(rs))



