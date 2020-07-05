All = int(input())

for q in range(0, All):
    temp=input().split()
    n=int(temp[0])
    k=int(temp[1])
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    for i in range(k):
        print(A[i],end=' ')
    print()