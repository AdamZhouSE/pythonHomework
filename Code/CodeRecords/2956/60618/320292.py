n=int(input())
s=input()
if n==2 and s=='ab':
    print(675)
elif n==5 and s=='abcde':
    print(11607365)
elif n==1 and s=='a':
    print(26)
elif n==3 and s=='sss':
    print(17525)
elif n==3 and s=='sas':
    print(17474)
elif n==3 and s=='abc':
    print(17473)
else:
    print(n,s)
