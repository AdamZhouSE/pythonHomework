n=input()
n1=n.count('b')+n.count('o')+n.count('y')
n2=n.count('bo')+n.count('oy')
res1=n1-n2
num1=n.count('g')+n.count('i')+n.count('r')+n.count('l')
num2=n.count('gi')+n.count('ir')+n.count('rl')

res2=num1-num2
print(res1)
print(res2,end='')
