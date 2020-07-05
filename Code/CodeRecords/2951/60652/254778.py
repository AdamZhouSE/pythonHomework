def bin_to_ter(a):
    l = len(a)
    Int_a = 0
    for i in range(0, l):
        if a[l - 1 - i] == '0':
            continue
        else:
            Int_a += 2 ** i
    remainder = 0
    quotient = Int_a
    ter_a = ''
    while quotient > 0:
        remainder = quotient % 3
        quotient = quotient // 3
        ter_a = str(remainder) + ter_a
    return ter_a


def bin_to_int(a):
    l = len(a)
    Int_a = 0
    for i in range(0, l):
        if a[l - 1 - i] == '0':
            continue
        else:
            Int_a += 2 ** i
    return Int_a

def toCompare(n1,n2):
    if len(n1)!=len(n2):
        return False
    index=0
    for i in range(len(n1)):
        if n1[i]!=n2[i]:
            index+=1
    if index!=1:
        return False
    else:
        return True


bin_n = input()
ter_n = input()
for i in range(0,len(bin_n)):
    if bin_n[i]=='0':
        tmp=bin_n[0:i]+'1'+bin_n[i+1:]
    else:
        tmp=bin_n[0:i]+'0'+bin_n[i+1:]
    if toCompare(bin_to_ter(tmp),ter_n):
        print(bin_to_int(tmp),end='')
        break