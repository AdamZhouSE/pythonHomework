li = []
while True:
    try:
        li.append(input())
    except EOFError:
        break
print(li)
