n=int(input())
num_list=list(map(int,input().split(" ")))
output=""
num=num_list.count(1)
print(num)
for i in range (1,n):
    if num_list[i]==1:
        output+=str(num_list[i-1])
        output+=" "
output+=str(num_list[len(num_list)-1])
print(output)