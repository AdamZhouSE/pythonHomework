num=list(input())
try:
    i=num.index('6')
    num[i]='9'
s=''.join(num)
print(s)