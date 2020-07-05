def son(A,n):
    cons=[]
    final=[]
    for i in range(len(A)-n+1):
        cons.append(A[i:i+n])
    for i in cons:
        final.append(sum(i))

    return max(final)

if __name__ == "__main__":
    numex=int(input())
    nextline=input().split(' ')
    n=int(nextline[0])
    q=int(nextline[1])
    opr=input().split(' ')
    opr=[int(x) for x in opr]
    nextline1=input().split(' ')
    n1=int(nextline1[0])
    q1=int(nextline1[1])
    opr1=input().split(' ')
    opr1=[int(x) for x in opr1]

    print(son(opr,q))
    print(son(opr1,q1))