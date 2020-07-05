string = input()
count = 0
for i in range(0, len(string)-2):
    if string[i] == "Q":
        for j in range(i+1, len(string) - 1):
            if string[j] == "A":
                for k in range(j+1, len(string)):
                    if string[k] == "Q":
                        count += 1
print(count, end="")