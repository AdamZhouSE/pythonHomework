num_list=eval(input())
output=[]
length=len(num_list)
num_list.sort()
for element in num_list:
    if not output or output[-1][-1]<element[0]:
        output.append(element)
    else:
        output[-1][-1]=max(output[-1][-1],element[1])
print(output)