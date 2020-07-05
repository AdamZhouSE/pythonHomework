s=input().replace(" ",'')
try:
    test=float(s)
    print(True)
except BaseException:
    print(False)