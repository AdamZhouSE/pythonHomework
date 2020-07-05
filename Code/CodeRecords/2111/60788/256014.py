def f(s):
    while s%2==0:
        s=int(s/2)
    while s%3==0:
        s=int(s/3)
    while s%5==0:
        s=int(s/5)
        
    return s==1

def h(s):
    if s==1:
        return 1
    else:
        count=1
        for i in range(2,1691):
            if f(i):
                count+=1
                if count==s:
                    return i
print(h(int(input().strip())))