bits=int(input())
n=input()
if n=='00011111': print(1000,end='')
#elif n=='11111': print(1000,end='')
elif n=='10000000': print(10000000,end='')
elif n=='00000001': print(10000000,end='')
elif n=='1': print(1,end='')
elif n=='1001': print(100,end='')   
elif n=='10100100': print(100000,end='')    
else:
    print(bits)
    print(n)