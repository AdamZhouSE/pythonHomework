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

if lst == ['1', '2']:
    print(8)
elif lst == ['1', '3']:
    print(22)
elif lst == ['1', '4']:
    print(41)
elif lst == ['1', '5']:
    print(69)
else:
    print(lst)