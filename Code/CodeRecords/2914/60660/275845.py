for i in range(t):
    result='YES'
    n=int(input())
    l=(eval('[' + input().replace(' ', ',') + ']'))
    m=eval('[' + input().replace(' ', ',') + ']')
    flag=0
    for j in range(n):
        if l[j]==m[j] and flag==1:
            flag=2
            continue
        if l[j]!=m[j]:
            if flag==0:
                x=l[j]-m[j]
                if x>0:
                    result='NO'
                    break
                flag=1
                continue
            if flag==1:
                if l[j]-m[j]!=x:
                    result='NO'
                    break
            if flag==2:
                result='NO'
                break
    if n==1:
        if l[0]>m[0]:
            result='NO'
    print(result)