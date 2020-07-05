lines = []
while True:
    try:
        lines.append(input())
    except:
        break
dishu=int(lines.pop(0))
zhishu=int(lines.pop(0).replace(",",""))
mi=dishu**zhishu
print(mi%1337)