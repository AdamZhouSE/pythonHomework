list=input().split("+")
num_list=[]
for num in list:
    num_list.append(int(num))
num_list.sort()
output=""
for time in range(len(num_list)-1):
    output+=f'{num_list[time]}'
    output+="+"
output+=f'{num_list[len(num_list)-1]}'
print(output)
