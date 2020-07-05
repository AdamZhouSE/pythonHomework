def pattern_out():
    N=int(input())
    temp=N
    flag=0
    change=0
    while True:
        if temp==N:
            flag+=1
        if flag==2:
            print(temp)
            break
        print(temp,end=" ")
        if temp<=0:
            change=1
        if change==0:
            temp-=5
        else:
            temp+=5

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        pattern_out()
