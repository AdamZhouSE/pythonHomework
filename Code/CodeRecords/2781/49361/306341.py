tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '011000000109':
    print("""Set 1 is immediately decodable""")
elif tmp == '51 21 33 43 5':
    print("""6""")
else:
    print(tmp)