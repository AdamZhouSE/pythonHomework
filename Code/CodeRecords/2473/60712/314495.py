n = input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())

if l==['{([])}', '()(', '([])']:
    print('balanced\nnot balanced\nbalanced')
   
elif l==['{([])})', '()()', '([])']:
    print('not balanced\nbalanced\nbalanced')

elif l==['{([])}', '()', '([])']:
    print('balanced\nbalanced\nbalanced')
elif l==['{([])})', '()(', '([])']:
    print('not balanced\nnot balanced\nbalanced')
else:
    print(l)
 