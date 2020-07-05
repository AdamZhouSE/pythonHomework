n_m=list(map(int,input().split(" ")))
n=n_m[0]
m=n_m[1]
a_list=list(map(int,input().split(" ")))
b_list=list(map(int,input().split(" ")))
output=""
for i in range(m):
    sum=0
    for j in range(n):
        if a_list[j]<=b_list[i]:
            sum+=1
    output+=str(sum)
    if i!=m-1:
        output+=" "
print(output)