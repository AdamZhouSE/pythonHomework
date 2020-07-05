str = list(input())
answer = ''
if str[0]=='-':
    answer += '-'
    str.remove('-')
for i in range(0,len(str)):
    answer += str[len(str)-i-1]
print(answer)