t=int(input())
while t>0:
    n=int(input())
    t=t-1
    i=0
    result=''
    num=1
    while n>0:
        i=i+1
        num=num*2
        n=n-num
    n=n+num
    if n==num:
        while i>0:
            result=result+'7'
            i=i-1
    else:
        while n>0:
            i=i-1
            if n-num//2>0:
                result=result+'7'
            else:
                result=result+'4'
            num=num//2
            if n==num:
                while i>0:
                    result=result+'7'
                    i=i-1
                break
            else:
                n=n%num
    print(int(result))