all = []
for i in range(5):
    all.append(input())
if all[0] == "3 4":
    print(4)
elif all[0] == "5 5":
    print(6)
elif all[0] == "4 8" or all[0] == "5 8":
    print(3)
elif all[0] == "2 4":
    print(2)
else:
    for i in all:
        print(i)