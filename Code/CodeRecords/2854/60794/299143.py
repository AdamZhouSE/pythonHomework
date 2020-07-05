a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
leg = 0
head = 0
body = 0
for i in range(len(a)):
    if a[i] == max(set(a), key=a.count):
        if leg < 4:
            leg = leg + 1
        else:
            if head == 0:
                head = a[i]
            else:
                body = a[i]
    else:
        if head == 0:
            head = a[i]
        else:
            body = a[i]
if leg != 4:
    print("Alien")
else:
    if head == body:
        print("Elephant")
    else:
        print("Bear")