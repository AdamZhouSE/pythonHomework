s= list(input())
sign = True
for i in range(s.__len__()):
    if s[i] != s[s.__len__()-1-i]:
        sign = False
print(sign)
