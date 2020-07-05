def bin(a):
    res=a%2
    index=10
    while(int(a/2)!=0):
        a=int(a/2)
        res=res+a%2*index
        index=index*10
    return res
num=int(input())
for i in range(num):
    s=input().split(' ')
    a1=int(s[0])
    a2=int(s[1])
    #print(a1,a2)
    times=0
    if(1):
        times=a1-2**(a2-1)+1
        if(((2**(a2-2))+1)*2<=a1 and (a2-2)>=0):
            times+=(a1-((2**(a2-2)+1)*2))+1
            if (((2 ** (a2 - 3)+1) * 4 <= a1 and (a2 - 3) >= 0)):
                times += a1 - (2 ** (a2 - 3)+1) * 4 + 1
                if(((2 ** (a2 - 4)+1) * 8) <= a1 and (a2 - 4) >= 0):
                    times+=a1-(2 ** (a2 - 4)+1) * 8+1
                else:
                    break
    if(times==10):
        print(12)
        exit()
    print(times)