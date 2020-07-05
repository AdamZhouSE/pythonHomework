li = []
for i in range(8):
    try:
        li.append(input())
    except EOFError:
        break


print(li)
