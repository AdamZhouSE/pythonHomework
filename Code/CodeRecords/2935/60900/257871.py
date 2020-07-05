str = input()
count = 0
count1 = 0
count2 = 0
index1 =[]
for i in range(0,len(str)):
    if str[i]=='A':
       index1.append(i)
for i in range(0,len(index1)):
    count1 = 0
    count2 = 0
    index = index1[i]
    for i in range(0,index):
        if str[i]=='Q':
            count1=count1+1
    for i in range(index+1,len(str)):
        if str[i]=='Q':
            count2=count2+1
    count = count +count1*count2


print(count,end='')
