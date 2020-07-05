T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(" ")]
    start,end=arr[0],arr[1]
    re=[]
    num=start
    while num<=end:
        if num==1:
            num=num+1
        else:
            mark=0
            for j in range(2,num-1):
               if num%j==0:
                  mark=1
                  break
            if mark==0:
                re.append(num)
            num=num+1
    for j in range(0,len(re)-1):
        print(re[j],end=" ")
    print(re[len(re)-1])

