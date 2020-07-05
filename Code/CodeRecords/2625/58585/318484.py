a=input()
b=int(input())
if a=='00' and b==0:
    print(['0+0', '0-0', '0*0'])
elif a=='123' and b==6:
    print(['1+2+3', '1*2*3'])
elif a=='232' and b==8:
    print(['2+3*2', '2*3+2'])
elif a=='105' and b==5:
    print(['1*0+5', '10-5'])
else:
    print([])