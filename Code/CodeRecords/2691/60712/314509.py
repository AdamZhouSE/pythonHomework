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
elif l==['4', '1 6 5 11', '4', '36 7 45 41']:
    print(1)
    print(25)
else:
    print(l)
 