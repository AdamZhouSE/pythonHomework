s=input()
result='True'
for i in range(0,len(s)):
    if s[i]>='0' and s[i]<='9':
        continue
    elif s[i]=='.':
        continue
    elif s[i]=='e':
        if i==len(s)-1:
            result='False'
            break
        else:
            continue
    else:
        result='False'
        break
print(result)