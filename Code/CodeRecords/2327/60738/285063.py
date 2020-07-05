String=input()
num=len(String)
num_list=[]
order_list=[]
for i in range (num+1):
    num_list.append(i);
for j in range(num):
    if String[j]=="I":
        order_list.append(num_list.pop(0))
    else:
        order_list.append(num_list.pop())
order_list.append(num_list.pop())
print(order_list)