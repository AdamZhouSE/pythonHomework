str = input()
sub=[]
for i in range(len(str)):
    temp = str[i]
    for j in range(i+1,len(str)):
        if str[j] not in temp:
            temp+=str[j]
        else:
            break

    sub.append(temp)

for i in range(len(sub)):
    sub[i]=len(sub[i])

print(max(sub))