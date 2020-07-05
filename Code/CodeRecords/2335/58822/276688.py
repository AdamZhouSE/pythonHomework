
a=int(input())
b=int(input())
times=0
if(a>b):
    print((a-b))
    exit()
else:
    c=a
    d=b
    min=0
    if(d<2*c):
        while(2*c>d):
            c=c-1
            times+=1
        if(2*c!=d):
            times=times+2
        else:
            times=times+1
        min=times
        k=(2*a-b)+1
        if(k<min):
            times=k
    else:
        while(c<d):
            times+=1
            c=c*2
            while(2*c>d):
                c = c - 1
                times += 1
            break
        if (2 * c != d):
            times = times + 2
        else:
            times = times + 1
print(times)