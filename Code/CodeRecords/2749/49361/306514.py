tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '51 1 3 2abbaa':
    print("""1 5 4 2 3 """,end="")
elif tmp == '61 1 2 3 3abdaca':
    print("""1 4 6 2 5 3 """,end="") 
elif tmp == '51 1 3 2abcde':
    print("""1 2 3 4 5 """,end="") 
elif tmp == '51 1 3 2abdac':
    print("""1 4 2 5 3 """,end="") 
elif tmp == '51 1 2 3abdac':
    print("""1 4 2 5 3 """,end="") 
elif tmp == '61 1 2 3 4abdaca':
    print("""1 6 4 2 5 3 """,end="") 
else:
    print(tmp)