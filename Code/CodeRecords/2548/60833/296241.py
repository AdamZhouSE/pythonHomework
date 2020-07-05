for i in range(0,int(input())):
    s=input()
    t=int(input())
    length=len(s)
    flag=0
    for j in range(length,0,-1):
        for k in range(0,length-j+1):
            temp=s[k:k+j]
            dict1 = {}
            for l in temp:
                dict1[l]=temp.count(l)
            zifu=list(dict1.keys())
            if len(zifu)==t:
                print(j)
                flag=1
                break
        if flag:
            break