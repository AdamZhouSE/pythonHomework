a=input()
cons='A'
cons=cons.split()
for i in range(1,int(a)):

    cons=cons*2
    cons.insert(len(cons)//2,chr(65+i))
print(''.join(cons))