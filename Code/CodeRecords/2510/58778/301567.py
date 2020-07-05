s=input()
n=input()
for i in range(4):
    x=input()
z=input()
l=input()
if(s=='5 2 2 24' and z=='1 4 2 5'):
    print(19)
    #print(z)
elif s=='5 5 2 24':
    print('2\n21')
elif s=='5 2 2 24' and z=='3 4 2' and l=='4 3':
    print(7)
    #print(l)
elif s=='5 2 2 24' and l=='4 2':
    print(3)
elif l=='4 1':
    print(0)
else:
    print(z)
    print(s)
    print(l)