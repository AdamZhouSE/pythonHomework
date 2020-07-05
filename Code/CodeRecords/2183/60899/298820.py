numOftests = int(input())
for i in range(numOftests):
    N = int(input())
    start = N*(N-1)+1
    end = (N+1)*N
    num = end-start+1
    print(int(num*(start+end)/2))