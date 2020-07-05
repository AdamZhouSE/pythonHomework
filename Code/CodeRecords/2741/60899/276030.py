str0 = input()
list0 = list(map(int,str0[1:len(str0)-1].split(",")))
length = []
maxlength = 0
for i in range(len(list0)):
    count = 0
    for j in range(len(list0)-1-i):
        if i+j == len(list0):
            count = j
            break
        if list0[i+j+1]>list0[i+j]:
            count +=1
        else:
            break
    length.append(count+1)

for h in length:
    if maxlength<h:
        maxlength = h
print(maxlength)