li = []
while True:
    try:
        li.append(input())
    except EOFError:
        break
li = sorted(li, key=lambda k: len(k))
print(li)

