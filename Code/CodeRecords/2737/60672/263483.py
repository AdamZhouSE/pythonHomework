def countnum(ar):
    ar=list(ar)
    br=[]
    count=0
    for i in range(len(ar)):
        b=ar[i]
        for j in range(i,len(ar)):
            if ar[j]==b:
                count+=1
        if count>int(len(ar)/3.0):
            br.append(b)
            count=0
        else:
            count=0
    print(br)

ar=input()
countnum(ar)