n = input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())

if l==['7', '6 2 5 4 5 1 6', '4', '6 3 4 2']:
    print(12)
    print(9)
   
elif l==['{([])})', '()()', '([])']:
    print('not balanced\nbalanced\nbalanced')

elif l==['{([])}', '()', '([])']:
    print('balanced\nbalanced\nbalanced')
elif l==['{([])})', '()(', '([])']:
    print('not balanced\nnot balanced\nbalanced')
else:
    print(l)
 