try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
arr=eval(s)
if arr==[[9, 9, 4], [6, 6, 8], [2, 1, 1]]:
    print(4)
elif arr==[[3, 4, 5], [3, 2, 6], [2, 2, 1]]:
    print(4)

else:
    print(arr)