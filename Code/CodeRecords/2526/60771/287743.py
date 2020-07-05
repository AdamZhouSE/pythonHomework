#03
root1 = input()
root2 = input()

root1 = eval(root1.replace("null","100"))
root2 = eval(root2.replace("null","100"))

outcome = []

for item in root1:
    if item != 100:
        outcome.append(item)
for item in root2:
    if item != 100:
        outcome.append(item)

outcome.sort()
print(outcome)
