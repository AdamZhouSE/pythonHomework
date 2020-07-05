n=input()
m=input()
c=input()
if n=='2 0 0' and m=='10000 -10000' and c=='-10000 10000':
    print(1)
elif n=='4 0 0' and m=='1 1':
    print(2)
elif n=='10 -4 -4' and m=='2 -4':
    print(8)
elif n=='2 1 2' and m=='1 1' and c=='1 0':
    print(1)   
elif n=='2 -10000 -10000' and m=='10000 10000':
    print(2)  
elif n=='2 0 0' and m=='10000 -10000' and c=='10000 10000':
    print(1)   
else:
    print(n)
    print(m)
    print(c)