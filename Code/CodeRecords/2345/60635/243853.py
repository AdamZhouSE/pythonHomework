count=int(input())
for i in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    curr = 1
    a, b = 0, 0
    for i in array:
        if i > curr:
            a = curr
            curr = i
        elif i == curr-1:
            b = i
            curr -= 1
        if a > 0 and b > 0:
            break
        curr += 1
    print(str(b)+' '+str(a))