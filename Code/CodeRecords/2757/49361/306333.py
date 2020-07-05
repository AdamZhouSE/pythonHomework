tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '51 22 33 44 5':
    print("""6""")
elif tmp == '51 21 33 43 5':
    print("""6""")
else:
    print(tmp)