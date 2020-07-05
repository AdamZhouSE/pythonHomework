n = int(input())
connell = [1,2,4,5,7,9,10,12,14,16,17,19,21,23,25,26,28,30,32,34]
for i in range(n):
    count = int(input())
    for j in range(count):
        if j != count-1:
            print(connell[j],end=' ')
        else:
            print(connell[j])