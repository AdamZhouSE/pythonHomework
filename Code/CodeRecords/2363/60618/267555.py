n=int(input())
binary=list(bin(n)[2:])
for i in range(0,len(binary)):
    if binary[i]=='0':
        binary[i]=='1'
    else:
        binary[i]=='0'
print(int(''.join(binary)))