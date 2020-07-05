n=input()
for i in range(len(n)):
    if n[i]=='6':
        n=n[0:i]+"9"+n[i+1:]
        break
print(n)