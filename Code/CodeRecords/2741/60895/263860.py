s=input().lstrip('[').rstrip(']').split(',')
max=1
for i in range(0,len(s)-1):
    if int(s[i])<int(s[i+1]):
        length=2
        for j in range(i+1,len(s)-1):
            if int(s[j])<int(s[j+1]):
                length=length+1
            else:
                break
        if max<length:
            max=length
print(max)