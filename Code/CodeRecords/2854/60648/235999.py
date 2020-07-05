list1 = input().split(" ")
list1 = [int(list1[i]) for i in range(len(list1))]
l = len(list1)
for i in range(l):
    count=0
    a=0
    b=0
    for j in range(l):
        if list1[i]==list1[j]:
            count=count+1
        else:
            a=b
            b=j
    if count>=4:
        if list1[a]==list1[b]:
            print('Elephant')
        else:
            print('Bear')
        break
    if i == l-1:
        print('Alien')
        break