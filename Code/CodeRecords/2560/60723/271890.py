T=int(input())
for i in range(T):
    N=int(input())
    temp=input().split()
    array=[[1 for _ in range(2)] for _ in range(N)]
    for j in range(N):
        array[j][1]=int(temp[j])
    array.sort()
    M=int(input())
    for j in range(N-1,0,-1):
        if array[j][1]==array[j-1][1]:
            array[j][0]=array[j][0]+array[j-1][0]
            array.pop(j-1)
    array.sort(reverse=True)
    for j in range(len(array)-1,-1,-1):
        if M>=array[j][0]:
            M=M-array[j][0]
            array.pop(j)
        else:
            break
    print(len(array))