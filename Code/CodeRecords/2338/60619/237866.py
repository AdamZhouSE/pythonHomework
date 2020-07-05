t = int(input())
for index in range(t):
    l = input().split(" ")
    len = int(l[0])
    x = int(l[1])
    numbers = input().split(" ")
    can = False
    for i in range(len-1):
        for j in range(i+1, len):
            if int(numbers[i])+int(numbers[j]) == x:
                can = True
                break
    if can:
        print("Yes")
    else:
        print("No")