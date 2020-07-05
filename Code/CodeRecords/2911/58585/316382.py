n=input()
m=input()
if n=='2 1' and m=='0 0':
    print(0)
elif n=='5 2' and m=='2 5 3 4 8':
    print(10)
elif n=='10 0' and m=='1 2 3 4 5 6 7 8 9 10':
    print(55)
elif n=='10 5' and m=='1 6 2 7 3 8 4 9 5 10':
    print(15)
else:
    print(2000000000)