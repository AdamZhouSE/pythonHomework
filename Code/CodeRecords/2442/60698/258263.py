def test():
    a=list(eval(input()))
    a.sort()
    if len(a)<=1:
        print(0)
        return
    else:
        max_diff=0
        for i in range(0,len(a)-1):
            if a[i+1]-a[i]>max_diff:
                max_diff=a[i+1]-a[i]
        print(max_diff)
        return 

test()
