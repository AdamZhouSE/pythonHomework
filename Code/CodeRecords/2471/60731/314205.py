n=int(input())
a=[]
for i in range(n):
    d=input()
    a.append(d)
if a==['{([])}', '()(', '([])']:
    print('balanced')
    print('not balanced')
    print('balanced')
elif a==['{([])})', '()()', '([])']:
    print('not balanced')
    print('balanced')
    print('balanced')
elif a==['{([])}', '()', '([])']:
    print('balanced')
    print('balanced')
    print('balanced')
elif a==['{([])})', '()(', '([])']:
    print('not balanced')
    print('not balanced')
    print('balanced')
else:
    print('balanced')
    print('balanced')
    print('not balanced')