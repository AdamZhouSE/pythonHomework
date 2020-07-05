import math
def Test():
    A=eval("["+input()+"]")
    A.sort()
    B=[]
    C=[]
    turn=0
    for i in range(0,math.ceil(len(A)/2)):
        if(turn==0):
            B.append(A[i])
            B.append(A[-1-i])
            turn=1
        else:
            C.append(A[i])
            C.append(A[-1 - i])
            turn=0
    print(sum(B)/len(B)==sum(C)/len(C))

if __name__ == "__main__":
    Test()