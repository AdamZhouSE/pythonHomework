def Test():
    N,X,Y=map(int,input().split())
    A = eval("[" + input().strip().replace(" ", ",") + "]")
    B = eval("[" + input().strip().replace(" ", ",") + "]")
    result=0
    equal=0
    for i in range(0,len(A)):
        if(A[i]>B[i]):
            result=result+A[i]
        elif(A[i]<B[i]):
            result=result+B[i]
        else:
            result=result+A[i]
    print(result)

if __name__ == "__main__":
    total = int(input())
    for i in range(0, total):
        Test()