num_list=list(map(int,input().split()))
num_list.reverse()
num_list.pop(0)
length=len(num_list)
output=""
for i in range(length):
    output+=str(num_list[i])
    if i!=length-1:
        output+=" "
print(output,end=" ")
    