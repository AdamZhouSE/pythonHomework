n=int(input())
for i in range(n):
    number=int(input())
    tem=[]
    for j in range(2**number):
        no=0
        binv = bin(j)[2:]
        binv = binv.zfill(number)
        word=list(binv)
        for k in range(number-1):
            if word[k]=="1" and word[k+1]=="1":
                no=1
        if no==0:
            tem.append(binv)
    print(len(tem))