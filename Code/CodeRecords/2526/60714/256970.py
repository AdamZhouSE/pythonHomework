temp = input()
try:
    a = eval(temp)
except:
    a = []
for item in eval(input()):
    a.append(item)
print(sorted(a))
