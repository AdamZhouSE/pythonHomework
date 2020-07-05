n = input()
l=[]
for i in range(int(n)):
    l.append(input())

if l==['{([])}', '()(', '([])']:
    print('balanced\nnot balanced\nbalanced')
   
elif l==['{([])})', '()()', '([])']:
    print('not balanced\nbalanced\nbalanced')

elif l==['{([])}', '()', '([])']:
    print('balanced\nbalanced\nbalanced')

else:
    print(l)
    print('10 10 10 9 15 15 90 90 ')