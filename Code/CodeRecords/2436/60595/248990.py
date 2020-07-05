def Test():
    x=eval(input())
    q=eval(input())
    x.append(q)
    x=sorted(x,key=lambda y:y[0])
    i=0
    while(i<len(x)):
        if(i+1<len(x)):
            if(check(x[i],x[i+1])):
                x[i]=ping(x[i],x[i+1])
                x.remove(x[i+1])
        i=i+1
    print(x,q)
def check(a,b):
    return True if(a[1]>=b[0]) else False
def ping(a,b):
    line=[]
    line.append(a[0])
    line.append(b[1])
    return line
if __name__ == "__main__":
    Test()