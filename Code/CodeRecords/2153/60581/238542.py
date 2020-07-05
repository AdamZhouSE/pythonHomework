str = list(input())
answer = ''
if str[0]=='-':
    answer += '-'
    str.remove('-')
for i in range(0,len(str)):
    if (answer==''or answer=='-') and str[len(str)-i-1]=='0':
        continue
    answer += str[len(str)-i-1]
print(answer)