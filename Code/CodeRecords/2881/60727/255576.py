a=int(input())
for x in range(0,a):
    if x>=(a+1)//2:
        i=a-x-1
    else:
        i=x
    numOfD=i*2+1
    numOfstar=(a-numOfD)//2
    st='*'*numOfstar+'D'*numOfD+'*'*numOfstar
    print(st)