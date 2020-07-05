n=input()
len=len(n)
n=n[1:len-1]
n=n.split(",")
n=list(map(int,n))

n.sort()
len=int((len-1)/2)
num=0
x=0
if(len<2):
    print("0")
else:
    while x<(len-1):
        if((n[x+1]-n[x])>num):
            num=n[x+1]-n[x]
        x+=1
    print(num)