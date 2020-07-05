list1 = list(map(int,input().split()))
list1.sort()
if list1[0]==list1[3]:
    if list1[4] != list1[5]:
        print("Bear")
    else:
        print("Elephant")
elif list1[1]==list1[4]:
        print("Bear")
elif list1[2]==list1[5]:
        print("Bear" if list1[0]<list1[1] else "Elephant")
else:
    print("Alien")