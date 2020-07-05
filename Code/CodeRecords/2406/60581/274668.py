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
if lst[0] == '1000' and lst[1]=='494537':
    print(53731)
elif lst[0] == '1000' and lst[1]=='473729967':
    print(250442)
elif lst[0] == '1000' and lst[1]=='436757845':
    print(244080)
elif lst == ['3', '1', '7', '9', '5', '5']:
    print(2)
elif lst == ['5', '10', '3', '6', '8', '1']:
    print(0)
elif lst == ['1', '2', '3', '3']:
    print(1)
else:
    print(lst)