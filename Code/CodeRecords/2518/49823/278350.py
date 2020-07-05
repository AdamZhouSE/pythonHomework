def al(a,b):
    l=[]
    a=sorted(a)
    b=sorted(b)
    p,r=0,0
    for i in range(len(a)):
        while(b[p]<a[i] and p<len(b)-1):
            p+=1
        if(p==0):
            d=abs(b[p]-a[i])
        else:
            d=min(abs(a[i]-b[p-1]),abs(b[p]-a[i]))
        r=max(r,d)
    print(r)

if __name__ == '__main__':
    al([int(i) for i in input().split(',')],[int(i) for  i in input().split(',')])
