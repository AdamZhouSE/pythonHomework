inp = input()
isTrue = True
for i in inp:
    if i.isalpha():
        if i != 'e':
            isTrue = False
            break
if isTrue:
    print(True)
else:
    print(False)

   