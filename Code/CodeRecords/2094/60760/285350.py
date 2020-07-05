source=input()
if source.count('e')>0:
    print('True')
try:
    res = int(source)
    print('True')
except :
    print('False')