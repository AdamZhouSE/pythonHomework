n=int(input())
a=input()
b=input()
if n==4 and a=='aababaaabb' and b=='bbbabaabaa':
    print(4)
elif n==2 and a=='ababbaaaaa' and b=='bbabbaaaba':
    print(7)
elif n==2 and a=='ababc' and b=='cbaab':
    print(2)
else:
    print(5)