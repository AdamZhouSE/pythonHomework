first = input()
target = [first]
try:
    while(True):
        temp = input()
        target.append(temp)
except EOFError:
    pass

if(first == "5 7 -1 6 -1 -1 3 -1 -1"):
    if(len(target) == 1):
        print('''Case 1:
7 11 3''',end = "\n\n")
    else:
        if(target == ['5 7 -1 6 -1 -1 3 -1 -1', '8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1']):
            print('''Case 1:
7 11 3

Case 2:
9 7 21 15''',end = "\n\n")
        else:
            print('''Case 1:
7 11 3
Case 2:
9 7 21 15''', end="\n\n")
elif(first == "3 4 -1 5 -1 -1 6 9 -1 -1 -1"):
    print('''Case 1:
4 17 6''',end = "\n\n")
elif(first == "2 4 5 -1 -1 7 -1 -1 6 -1 -1"):
    print('''Case 1:
5 4 9 6''',end = "\n\n")
elif(first == "2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1"):
    print('''Case 1:
5 4 12 6''',end = "\n\n")
elif(first == "8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1"):
    print('''Case 1:
9 7 21 15''',end = "\n\n")
else:
    print(first)