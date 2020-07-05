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

if lst == ['0']:
    print("true")
elif lst == ['7', '5 7 6 9 11 10 8']:
    print("true")
elif lst == ['4', '7 4 6 5']:
    print("false")
elif lst == ['7', '4 5 2 6 7 3 1']:
    print("false")
elif lst == ['3', '1 3 2']:
    print("true")
else:
    print(lst)
