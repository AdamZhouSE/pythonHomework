sum = int(input())
maxnum = max([int(i) for i in str(sum)])
list = ['' for i in range(maxnum)]

for i in range(len(str(sum))):
    middle = int(str(sum)[i])
    for j in range(len(list)):
        if(j<middle):
            list[j] = list[j]+'1'
        elif(list[j]!=''):
            list[j] = list[j] + '0'
list = [list[i]+' ' for i in range(len(list))]
list = "".join(list)
print(maxnum)
print(list[0:-1])