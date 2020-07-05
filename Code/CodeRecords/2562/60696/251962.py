def print_in_form(arr):
    if len(arr) == 0:
        print('EMPTY')
        return
    for i in arr:
        print(i, end=' ')
    print()


n = int(input())
for i in range(n):
    unread = []
    read = []
    trash = []
    arr = input().split()
    num = int(arr[0])
    temp = int(arr[1])
    operations = [int(j) for j in input().split()]
    for j in range(num):
        unread.append(j+1)
    for j in range(temp):
        command = operations[2 * j]
        operand = operations[2 * j + 1]
        if command == 1:
            unread.remove(operand)
            read.append(operand)
        elif command == 2:
            read.remove(operand)
            trash.append(operand)
        elif command == 3:
            unread.remove(operand)
            trash.append(operand)
        elif command == 4:
            trash.remove(operand)
            read.append(operand)
    print_in_form(unread)
    print_in_form(read)
    print_in_form(trash)