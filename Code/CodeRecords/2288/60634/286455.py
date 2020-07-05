#main-----
while True:
    temp = input().split(' ')
    m = int(temp[0])
    n = int(temp[1])
    if m == 0 and n == 0:
        break
    stack = [m]
    count = 0
    while len(stack) >0:
        i = stack.pop()
        count += 1
        if 2*i <= n:
            stack.append(2*i)
            if 2*i+1 <= n:
                stack.append(2*i+1)
    print(count)






























