def f():
    a=input().split(',')
    a=list(map(int,a))
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j] and j-i>1:
                return False
    return True


print(f())