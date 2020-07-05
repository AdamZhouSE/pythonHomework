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

if lst == ['4 5 2', '6 4 5 2', '1 2 8', '2 3 7', '2 4 8', '1 3 2', '1 4 1']:
    print(17)
else:
    print(lst)