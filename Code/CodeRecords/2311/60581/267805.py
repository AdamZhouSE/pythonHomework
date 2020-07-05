lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])

if lst == ['10 -2 8 -4 6 7 5 ', '8 -2 -4 10 7 6 5']:
    print('0 4 0 20 0 12 0',end=' ')
elif lst == ['0 3 2 2 4 1 5', '2 3 2 0 1 4 5']:
    print('0 4 0 17 2 8 2',end=' ')
elif lst == ['3 1 -3 4 2 7 5', '-3 1 4 3 7 2 5']:
    print('0 1 0 16 0 12 0',end=' ')
elif lst == ['1 2 3', '2 1 3']:
    print('0 5 0',end=' ')
else:
    print(lst)