src=input()
minus=False
if src[0]=='-':
    minus=True
    src=src[1:]
src=list(src)


def reverse(src):
    l = len(src)
    if l<=1:
        return
    src[0],src[-1]=src[-1],src[0]
    reverse(src[1:l-1])


reverse(src)
if src[0]=='0':
    src=src[1:]
if minus:
    print('-',end='')
print(''.join(src))