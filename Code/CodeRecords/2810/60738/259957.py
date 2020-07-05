n=input()
num_list=[]
for i in range(len(n)):
    num_list.append(int(n[i]))
length=max(num_list)
print(str(length))
output=""
for k in range(length):
    num=0
    for j in range(len(n)):
        if num_list[j]>0:
            num_list[j]-=1
            num+=10**(len(n)-j-1)
    output+=str(num)
    if k!=length-1:
        output+=" "
print(output)            
