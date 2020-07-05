arr = []
while True:
    tmp = input()
    if tmp == ']':
        break
    if tmp == '[':
        continue
    tmp = tmp.replace("\"", "").replace(",","")
    print(tmp)
