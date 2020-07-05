n=int(input())
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    output=""
    for i in range(len(num_list)-1):
        if num_list[i]>=max(num_list[i+1:]):
            output+=str(num_list[i])+" "
    output+=str(num_list[len(num_list)-1])
    print(output)