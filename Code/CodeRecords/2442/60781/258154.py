n=input()

n=n.split(",")
n=list(map(int,n))
n.sort()
len=len(n)
num=0
x=0
while x<(len-1):
    if(n[x+1]-n[x]>num):
        num=n[x+1]-n[x]
    x+=1
print(num)