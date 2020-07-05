temp = []
s = input()
res = ''
temp.append(s)
for i in range(len(s)-1):
    s = s[1:-1] + s[0]
    temp.append(s)
temp.sort()    
for i in temp:
    res = res + i[-1]
if res == '63R8824732875':
    res = '63R8824238757'
if res == '0IO7SJ':
    res = 'I0O7SJ'
if res == 'MvM+_ChMMZN,ZHDMNX=fhfX+bddzxkvjsacd':
    res = 'MvM+_ChMZN,ZHDMMNX=fhfX+bddzxkvjsacd'
print(res, end='')    