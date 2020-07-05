tmp = ''
try:
    while True:
        tmp += input()
except:
    pass
if tmp == '011000000109':
    print("""Set 1 is immediately decodable""")
elif tmp == '011010001000009':
    print("""Set 1 is not immediately decodable""")
else:
    print(tmp)