def toRom(n):
    str1=""
    dic={'1000': 'M', '900': 'CM', '500': 'D', '400': 'CD', '100': 'C', '90': 'XC', '50': 'L', '40': 'XL', '10': 'X', '9': 'IX', '5': 'V', '4': 'IV', '1': 'I'}
    for i,j in dic.items():
        temp=n//int(i)
        if temp!=0:
            str1=str1+temp*j
            n=n-temp*int(i)
    return str1

n=int(input())
print(toRom(n))