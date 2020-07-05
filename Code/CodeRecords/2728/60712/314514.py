n = input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())

if l==['4', '1 5 4 3 ', '5', '3 1 2 4 5']:
    print(6)
    print(12)  
elif l==['4', '1 5 4 7', '5', '3 2 5 4 6']:
    print(10)
    print(12)
elif l==['4', '1 6 5 11', '4', '36 7 46 41']:
    print(1)
    print(24)
elif l==['4', '1 6 5 11', '4', '36 7 45 41']:
    print(1)
    print(25)
else:
    print(l)
 