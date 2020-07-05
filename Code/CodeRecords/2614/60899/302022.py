numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    cnt = 0
    for j in range(length):
        for k in range(length):
           if A[j] == B[j]+C[k]:
               cnt+=1;
    print(cnt)