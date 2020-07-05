sum = int(input())
num = int(str(sum)[0])
list = ['' for i in range(num)]

for i in range(len(str(sum))):
    middle = int(str(sum)[i])
    for j in range(len(list)):
        if(j<middle):
            list[j] = list[j]+'1'
        else:
            list[j] = list[j] + '0'
list = [list[i]+' ' for i in range(len(list))]
list = "".join(list)
print(sum)
print(list[0,-1])