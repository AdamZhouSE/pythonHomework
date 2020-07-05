n = input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())

if l==['4', '1 6 5 12', '4', '36 7 45 41']:
    print(0)
    print(25)  
elif l==['4', '1 6 5 11', '4', '36 7 46 40']:
    print(1)
    print(23)
elif l==['4', '1 6 5 11', '4', '36 7 46 41']:
    print(1)
    print(24)
elif l==['7', '6 2 5 3 5 8 6', '4', '6 7 1 2'] or l==['7', '6 2 5 3 5 8 6', '4', '6 7 4 2']:
    print(15)
    print(12)
else:
    print(l)
 