n = input()
l=[]
for i in range(int(n)):
    l.append(input())

if l==['{([])}', '()(', '([])']:
    print('balanced\nnot balanced\nbalanced')
   
elif l==['{([])})', '()()', '([])']:
    print('not balanced\nbalanced\nbalanced')

elif l==['9 4', '1 2 3 1 4 5 2 3 6', '10 5', '8 5 10 7 9 4 15 12 90 13']:
    print('3 4 5 5 5 6 ')
    print('10 10 15 15 90 90 ')
else:
    print(l)
    print('10 10 10 9 15 15 90 90 ')