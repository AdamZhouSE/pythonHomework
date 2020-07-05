if __name__ == '__main__':
    A=input()
    B=input()
    A_length=len(A)
    B_length=len(B)
    time=0
    for x in range(0,A_length-B_length+1):
        issame=1
        for y in range(0,B_length):
            if not A[x+y]==B[y]:
                issame=0
        if issame==1:
            time+=1

    print(time,end='')