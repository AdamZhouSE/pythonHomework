import operator
start=input()
end=input()
if start.replace('X','') != end.replace('X', ''):
    print("False")
i=0
for (symbol, op) in (('L', operator.ge), ('R', operator.le)):
    B = (i for i, c in enumerate(end) if c == symbol)
    for i, c in enumerate(start):
        if c == symbol and not op(i, next(B)):
            i=0
        else:
            i=1
if i==0:
    print("False")
else:
    print("True")

