s=input()
ls=[]
while True:
    try:
        ls.append(s)
        s=input()
    except EOFError:
        break
print(ls)