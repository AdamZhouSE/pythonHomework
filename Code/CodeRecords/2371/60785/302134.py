t= int (input())
for g in range(t):
    s = input()
    numalpha=[]
    for i in s:
        if i.isalpha() or i.isdigit():
            numalpha.append(i)