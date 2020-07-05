def question31():
    num = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    del l1[0]
    del l2[0]
    record = []
    while not len(l1) == 0 and not len(l2) == 0:
        if not record.__contains__(l1+l2):
            record.append(l1+l2)
        else:
            return -1
        if l1[0] > l2[0]:
            temp1 = l1[0]
            temp2 = l2[0]
            del l1[0]
            del l2[0]
            l1.append(temp2)
            l1.append(temp1)
        else:
            temp1 = l1[0]
            temp2 = l2[0]
            del l1[0]
            del l2[0]
            l2.append(temp1)
            l2.append(temp2)
            
    if len(l2) == 0:
        return str(len(record)) + ' ' + str(1)
    else:
        return str(len(record)) + ' ' + str(2)

if __name__ == '__main__':
    print(question31())