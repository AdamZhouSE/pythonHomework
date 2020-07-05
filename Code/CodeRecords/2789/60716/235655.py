num = int(input())
listforanswer = []
for i in range(num):
    amount = int(input())
    str = input().split(' ')
    lists = [int(i) for i in str]
    lists.sort()
    lists.reverse()
    index=1
    print(lists)
    for i in range(amount):
        print(i)
        if lists[i]<i+1:
            index=i
            print(True)
            break
    listforanswer.append(index)
for i in listforanswer:
    print(i)