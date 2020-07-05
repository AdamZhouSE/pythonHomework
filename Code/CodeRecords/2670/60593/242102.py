t=int(input())
for i in range(t):
    x=int(input())
    s=bin(x).replace('0','2').replace('1','0').replace('2','1')
    print(oct(int(s.replace('1','0',1),base=2))[2:])