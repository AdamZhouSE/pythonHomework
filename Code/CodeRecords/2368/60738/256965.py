n=int(input())
for i in range(n):
    output=""
    length=int(input())
    num_list=list(map(int,input().split()))
    for j in range(length):
        if j%2==0:
            output+=str(num_list[-int((j+2)/2)])
            output+=" "
        else:
            output+=str(num_list[int((j-1)/2)])
            output+=" "
    print(output)