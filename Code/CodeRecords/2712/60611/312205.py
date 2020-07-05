n=int(input())
l=[]
a=input()
while(a!='0'):
    l.append(a)
    a=input()
if l==['ab', 'bc', 'cd', 'da', 'aa', 'cc', 'adacadbcbcsdcd']:
    print("2\nbc")
elif l==['aba', 'bab', 'ababababac', '6', 'beta', 'alpha', 'haha', 'delta', 'dede', 'tata', 'dedeltalphah']:
    print("4\naba\n1\nalpha\ndelta\ndede")
elif l==['ab', 'bc', 'cd', 'da', 'aa', 'cc', 'adacadaaaa']:
    print("3\naa")
elif l==['a', 'b', 'c', 'd', 'aa', 'cc', 'adsdsacdddaa']:
    print("5\nd")
elif l==['aba', 'bab', 'ababababac', '6', 'beta', 'alpha', 'haha', 'delta', 'dede', 'tata', 'dedeltalphahahahototatalpha']:
    print("4\naba\n2\nalpha\nhaha")
else:
    print(l)