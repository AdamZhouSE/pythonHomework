import math
def greatnum(N,A,B):
    count=0
    i=min(A,B)
    rem=0
    if math.log(A,B)%1==0:      
        print(int(N*B%(math.pow(10,9)+7)))
    elif math.log(B,A)%1==0:
        print(int(N*A%(math.pow(10,9)+7)))
    else:
        while(count<N):
            if i%A==0 or i%B==0:
                rem=i
                count=count+1
            i=i+1
        print(int(rem%(math.pow(10,9)+7)))
N=int(input())
A=int(input())
B=int(input())
greatnum(N,A,B)