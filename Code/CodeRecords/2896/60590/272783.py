newspaper = input()
mail = input()

newspaper = list(newspaper)
mail = list(mail)

#print(newspaper)
#print(mail)

flag = True
while flag:
    for i in range(mail.__len__()):
        for j in range(newspaper.__len__()):
            if mail[i] == ' ':
                continue
            else:
                if newspaper[j] == mail[i]:
                    newspaper[j] = ''
                    break
                else:
                    flag = False

if flag:
    print("YES")
else:
    print("NO")