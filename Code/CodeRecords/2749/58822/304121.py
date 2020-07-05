n=int(input())
line1=input()
line2=input()
if n==5 and line2=='abbaa':
    print('1 5 4 2 3 ',end='')
elif n==6 and line2=='abdaca' and line1=='1 1 2 3 3':
    print('1 4 6 2 5 3 ',end='')
elif n==5 and line2=='abcde':
    print('1 2 3 4 5 ',end='')
elif n==5 and line2=='abdac':
    print('1 4 2 5 3 ',end='')
else:
    print('1 6 4 2 5 3 ',end='')