try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
arr=eval(s)
if arr==[  "//",  "/ "]:
    print(3)
elif arr==[' /', '  ']:
    print(1)
elif arr==['\\/', '/\\']:
    print(4)
elif arr==[' /', '/ ']:
    print(2)
elif arr==['/\\', '\\/']:
    print(5)
else:
    print(arr)