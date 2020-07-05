n=input()
num_list=[]
for i in range(len(n)):
    num_list.append(int(n[i]))
print(str(max(num_list)))
output=""
for k in range(max(num_list)):
    num=0
    for j in range(len(n)):
        if num_list[j]>0:
            num_list[j]-=1:
                num+=10**j
    output+=str(num)
    if k!=len(n)-1:
        output+=" "
print(output)            
