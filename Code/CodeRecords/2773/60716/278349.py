lists = list()
input()
while True:
    try:
        t = eval(input())
        lists.append(t)
    except:
        break
print(lists)