newspaper = list(input())
letter = list(input())
for i in letter:
    if i == " ":
        continue
    if newspaper.count(i) != 0:
        newspaper.remove(i)
    else:
        print("NO",end = "")
        break
else:
    print("YES",end = "")