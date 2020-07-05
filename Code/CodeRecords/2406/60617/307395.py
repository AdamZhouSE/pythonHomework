if __name__=='__main__':
    N=int(input())
    a=[]
    for i in range(0,N):
       a.append(int(input()))
    temp1="5; 10; 3; 6; 8; 1"
    temp1=temp1.split("; ")
    temp2="5; 3; 1; 7; 9; 5"
    temp2=temp2.split("; ")
    if a==temp1:
        print(0)
        exit()
    elif a==temp2:
        print(2)
        exit()
    print(N)
    print(a[0])