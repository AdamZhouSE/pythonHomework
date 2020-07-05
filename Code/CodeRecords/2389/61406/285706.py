T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    for i in range(0,N//2):
        temp = source[2*i]
        source[2*i]=source[2*i+1]
        source[2*i+1]=temp
    for i in range(0,N-1):
        print(source[i],end=' ')
    print(source[N-1])