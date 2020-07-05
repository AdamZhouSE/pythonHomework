equations=eval(input())
flag='true'
for eq in equations:        
    if eq[1]=='!':
        if eq[0] == eq[-1]:
            flag='false'
print(flag)