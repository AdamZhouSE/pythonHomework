a = input().split()
num = int(a[0])
s = int(a[1])
b = []
for i in range(num):
    b.append(eval(input()))
for i in range(num):
    if(i==num-1):
        print(0)
        break
    head = i
    length = 2
    tail = i + length - 1
    up = b[i]
    down = b[i + 1]
    while head + length-1  < num:
        if up <= s and down <= s:
            up += (b[head + int(length / 2)])
            if head+length+1>=num:
                length+=2
                break
            down += (b[head + length] + b[length + head + 1] - b[head + int(length / 2)])

        else:
            break
        length += 2

    print(length - 2)
