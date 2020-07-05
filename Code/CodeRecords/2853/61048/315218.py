def arr25():
    n=int(input())
    cookies=[int(x) for x in input().split(' ')]
    sumc=sum(cookies)
    cnt=0
    if(sumc%2==0):
        for num in cookies:
            if(num%2==0):
                cnt+=1
    else:
        for num in cookies:
            if(num%2==1):
                cnt+=1
    print(cnt)
    return

arr25()