newspaper = input()
mail = input()

newspaper = list(newspaper)
mail = list(mail)

#print(newspaper)
#print(mail)

flag = True
for i in range(mail.__len__()):
    if mail[i] == ' ':
        continue
    else:
        for j in range(newspaper.__len__()):
            if newspaper[j] == ' ':
                continue
            else:
                if newspaper[j] == mail[i]:
                    flag = True
                    newspaper[j] = '1'
                    break
                else:
                    flag = False
                    break

if flag:
    print("YES", end="")
else:
    print("NO", end="")

