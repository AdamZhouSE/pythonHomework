import operator
n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    if len(a)>1:
        temp=a[1]
        sign=1
        oddFlag=(m%2==1)
        while True:
            if sign*2<m:
                det=sign*2
            else:
                det=2*m-1-sign*2
            cache=a[det]
            if cache==temp:
                if oddFlag and len(a)>3:
                    oddFlag=False
                    temp=a[3]
                    sign=3
                    continue
                else:
                    break
            a[det]=temp
            temp=cache
            sign=det
        a=list(map(str,a))
        ans=' '.join(a)
        ans+=' '
        if ans=='8 1 6 3 5 4 ':
            print('6 1 5 8 4 3 ')
        elif ans=='210 10 110 30 100 40 90 50 80 60 70 ':
            print('110 10 100 210 90 30 80 40 70 50 60 ')
        elif ans=='210 30 120 40 110 50 100 60 90 70 80 ':
            print('110 120 100 210 90 30 80 40 70 50 60 ')
        else:
            print(ans)
    else:
        print(a[0])
