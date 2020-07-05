num = int(input())
listforanswer = []
for i in range(num):
    amount = int(input())
    str = input().split(' ')
    lists = [int(i) for i in str]
    lists.sort()
    index=1
    for i in range(1,num):
        if num-i>0 and lists[num-i]>index:
            index+=1
        else:
            break;
    listforanswer.append(index)
for i in listforanswer:
    print(i)