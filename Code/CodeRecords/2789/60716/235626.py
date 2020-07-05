num = int(input())
listforanswer = []
for i in range(num):
    amount = int(input())
    str = input().split(' ')
    lists = [int(i) for i in str]
    lists.sort()
    lists.reverse()
    index=0
#    print(lists)
    for i in range(len(lists)):
#        print("1")
        if lists[i]<i+1:
            index=i
#            print(True)
            break
    listforanswer.append(index)
for i in listforanswer:
    print(i)