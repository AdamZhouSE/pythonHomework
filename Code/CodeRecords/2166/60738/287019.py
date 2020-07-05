num=int(input())
num_list=[]
ok_list=[]
for i in range (num):
    num_list.append(int(input()))
def place(num):
    temp_list=[]
    for j in range(num):
        temp_list.insert(0,num-j)
        for k in range(num-j):
            temp_letter=temp_list.pop()
            temp_list.insert(0,temp_letter)
    return temp_list
for element in num_list:
    ok_list=place(element)
    for t in range(len(ok_list)):
        if t!=len(ok_list)-1:
            print(str(ok_list[t])+" ",end="")
        else:
            print(str(ok_list[t]))
    
