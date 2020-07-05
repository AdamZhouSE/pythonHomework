string=input()
num_list=list(map(int,string))
flag=False
for i in range(len(num_list)-1):
    for k in range(i+1,len(num_list)):
        if(num_list[i]<num_list[k]):
            if(num_list[k]==max(num_list[k:])):
                letter=num_list[i]
                num_list[i]=num_list[k]
                num_list[k]=letter
                flag=True
                break
    if flag:
        break
for element in num_list:
    print(str(element),end="")
print()

