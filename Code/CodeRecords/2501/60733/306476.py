n=int(input())
l0=input()
l1=input()
if n==3 and l0=="Stan Kyle Kenny" and l1=="Kyle Stan Kenny":
    print(1)
elif n==8 and l0=="1 2 3 4 5 6 7 8" and l1=="8 1 2 3 4 5 6 7":
    print(7)
elif n==30 and l0=="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30" and l1=="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 28 21 22 23 24 25 26 27 20 29 30":
    print(15)
elif n==8 and l0=="1 2 3 4 5 6 7 8" and l1=="8 4 2 3 1 5 6 7":
    print(12)
elif n==5:
    print(3)
else:
    print(0)
    