def connell(num):
    n = 0
    i = 1
    current = 1
    total = ""
    while n < num:
        if num-n < i:
            for j in range(num-n):
                total = total+str(current)
                if j != num-n-1:
                    total = total+" "
                current = current+2
            current = current-1
        else:
            for j in range(i):
                total = total+str(current)
                if j+1+n != num:
                    total = total+" "
                current = current+2
            current = current-1
        n = n+i
        i = i+1
    return total


total = int(input())
num = []
for i in range(total):
    num.append(int(input()))
for i in range(total):
    print(connell(num[i]))