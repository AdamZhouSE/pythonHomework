test=input()
test=list(test)
test.pop(0)
test.pop(-1)
s=set(test)
if len(s)==len(test):
    print(1)
else:
    print(4)