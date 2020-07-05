from enum import Enum


class Teen(Enum):
    Ten = '0'
    Eleven = '1'
    Twelve = '2'
    Thirteen = '3'
    Fourteen = '4'
    Fifteen = '5'
    Sixteen = '6'
    Seventeen = '7'
    Eighteen = '8'
    Nineteen = '9'


class Ty(Enum):
    Twenty = '2'
    Thirty = '3'
    Forty = '4'
    Fifty = '5'
    Sixty = '6'
    Seventy = '7'
    Eighty = '8'
    Ninety = '9'


s = input()
n = len(s)

if n == 0:
    print('Zero')
    exit()

i = n % 3
a = n // 3
ar = []
if i > 0:
    ar.append(s[:i])
for q in range(a):
    ar.append(s[q * 3 + i:q * 3 + 3 + i])
ar.reverse()

ans = ''

figure3 = ['', 'Thousand', 'Million', 'Billion']
num = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', "Eight", 'Nine']
figure = ['', '', 'Hundred']

if i == 1:
    si = ar[a][::-1]
    ans += num[int(si[0])] + ' '
    ans += figure3[a] + ' '
if i == 2:
    si = ar[a][::-1]
    if si[1] == '1':
        ans += Teen(si[0]).name+' '
    else:
        ans += Ty(si[1]).name+' '
        ans += num[int(si[0])]+' '
    ans += figure3[a]+' '

a -= 1

while a >= 0:
    si = ar[a][::-1]
    ans += num[int(si[2])]+' '
    ans += figure[2]+' '
    if si[1] == '1':
        ans += Teen(si[0]).name+' '
    else:
        ans += Ty(si[1]).name+' '
        ans += num[int(si[0])]+' '
    ans += figure3[a]+' '
    a -= 1

print(ans.strip())

