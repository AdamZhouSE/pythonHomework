composition = input()
length = 0
for i in composition:
    if i != " ":
        length = length + 1
print(length,end = "")