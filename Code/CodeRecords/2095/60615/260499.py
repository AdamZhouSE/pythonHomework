num_1 =input()
num_2 =input()

def bin_to_dec(n):
    num=[i for i in n]
    num.reverse()
    value=0
    for i in range(0,len(num)):
        value=value+int(num[i])*2**i
    return value

def dec_to_bin(num):
    value=''
    while num>0:
        value=str(num%2)+value
        num=num//2
    return value

result=dec_to_bin(bin_to_dec(num_2)+bin_to_dec(num_1))
print(result)