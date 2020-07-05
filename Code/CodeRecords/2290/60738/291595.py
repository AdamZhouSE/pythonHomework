n=int(input())
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    output=""
    for i in range(N-1):
        if num_list[i]>num_list[i+1]:
            output+=str(num_list[i+1])
            output+=" "
        else:
            output+=str(-1)
            output+=" "
    output+=str(-1)
    output+=" "
    print(output)
        