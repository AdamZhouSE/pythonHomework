test=input()
test=list(test)
test.pop(0)
test.pop(-1)
t=str(''.join(test)).split(',')
s=set(test)
if len(s)==len(test):
    print(1)
else:
    print(1)