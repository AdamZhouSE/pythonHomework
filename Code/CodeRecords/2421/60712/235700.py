n = input()
result = n
for i in range(len(n)):
    if n[i:i+1]=="6":
        if i==len(n)-1:
            result = n[0:i]+"9"
            break
        else:
            result = n[0:i]+"9"+n[i+1:len(n)]
            break
print(int(result))