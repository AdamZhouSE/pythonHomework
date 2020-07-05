t= int (input())
for g in range(t):
    s = input()
    numalpha=[]
    for i in s:
        if  i.isdigit() or i.isupper():
            numalpha.append(i)
        if i.islower():
            numalpha.append(chr(ord(i)-32))
    print(numalpha)