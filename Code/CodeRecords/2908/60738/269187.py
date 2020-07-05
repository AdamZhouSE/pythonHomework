n=int(input())
num_list=[]
temp_list=[]
for i in range(n):
    String=input().strip()
    temp_list.append(String)
    num_list.append("".join(sorted(String)))
num_list1=set(num_list)
print(len(num_list1),end="")

    
    
    