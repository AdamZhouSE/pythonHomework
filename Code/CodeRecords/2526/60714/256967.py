temp = input()
if temp != "null":
    a = eval(temp)
else:
    a = []
for item in eval(input()):
    a.append(item)
print(sorted(a))
