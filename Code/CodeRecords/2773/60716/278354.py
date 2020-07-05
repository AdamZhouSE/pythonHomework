lists = list()
input()
while True:
    t = input()
    if t==']':
        break
    else:
        temp = eval(t.split(','))
        lists.append(t)
print(lists)