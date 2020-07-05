def arr1():
    line1=input().split(' ')
    nA=int(line1[0])
    nB=int(line1[1])
    line2 = input().split(' ')
    k,m=int(line2[0]),int(line2[1])
    A=[int(x) for x in input().split(' ')]
    A.sort()
    B = [int(x) for x in input().split(' ')]
    B.sort(reverse=True)
    tmpA=A[k-1]
    tmpB=B[m-1]
    if(tmpA<tmpB):
        print("YES")
    else:
        print("NO")
    return

arr1()