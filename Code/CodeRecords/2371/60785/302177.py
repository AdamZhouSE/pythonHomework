t= int (input())
for g in range(t):
    res="YES"
    s = input()
    numalpha=[]
    for i in s:
        if  i.isdigit() or i.isupper():
            numalpha.append(i)
        if i.islower():
            numalpha.append(chr(ord(i)-32))
    for i in range(len(numalpha)):
        if numalpha[i]!=numalpha[len(numalpha)-1-i]:
            res="NO"
            
    print(res)                     
        