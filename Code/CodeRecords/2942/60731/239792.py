n=int(input())
num=input()
l=num.split()
l.sort(reverse=True)
result=''.join(l)
num1=int(result)
print(result,end='')


