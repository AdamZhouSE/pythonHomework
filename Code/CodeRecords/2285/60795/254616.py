T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    if num==1:
        print("没有利润")
    else:
        re=[]
        start,max=0,0
        small,during=0,0
        for j in range(1,num):
            if arr[j]>arr[j-1]:
                max=j
            else:
                if arr[j]>arr[start]:
                    small=j
                    during=arr[max]-arr[start]
                    continue
                else:
                    if j-start>1:
                       re.append(start)
                       re.append(j-1)
                    start=j
        if max>0:
            if small>0:
                two=(arr[max]-arr[small])+(arr[small-1]-arr[start])
                one=arr[max]-arr[start]
                if two>one:
                    re.append(start)
                    re.append(small-1)
                    re.append(small)
                    re.append(max)
                else:
                    re.append(start)
                    re.append(max)
            else:
                re.append(start)
                re.append(max)
        if len(re)==0:
            print("没有利润")
        else:
            k=0
            while k<len(re)-2:
                print("(",end="")
                print(re[k],end=" ")
                print(re[k+1],end="")
                print(")",end=" ")
                k=k+2
            print("(",end="")
            print(re[len(re)-2],end=" ")
            print(re[len(re)-1],end="")
            print(")")
           