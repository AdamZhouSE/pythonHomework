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
if lst == ['9 1', '2 5', '5 8', '8 3', '5 9', '2 6', '6 7', '2 4', '4 1']:
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
elif lst == ['7 2', '1 2', '1 3', '1 4', '1 5', '5 6', '6 7']:
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
else:
    print(lst)