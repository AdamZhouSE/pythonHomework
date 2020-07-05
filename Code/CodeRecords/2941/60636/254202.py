n=int(input())
source=list(input())
sums=0
for i in range(n):
    if(source[i]=="A"):
        sums=sums+4
    elif(source[i]=="B"):
        sums=sums+3
    elif(source[i]=="C"):
        sums=sums+2
    elif(source[i]=="D"):
        sums=sums+1
    elif(source[i]=="F"):
        sums=sums+0
print("{:14f}".format(sums/n))