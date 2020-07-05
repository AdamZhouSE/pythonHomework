string=input()
houzhui_list=[]
length=len(string)
output=""
for i in range(0,length):
    houzhui_list.append([string[i:],i+1])
houzhui_list.sort()
for j in range(length):
    output+=str(houzhui_list[j][1])
    if j !=length-1:
        output+=" "
print(output)