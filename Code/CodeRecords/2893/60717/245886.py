list1=eval(input())
while True:
    tmp=list1[0]
    list1.remove(tmp)
    if tmp in list1:
        list1.append(tmp)
    else:
        print(tmp)
        break