number=eval(input())
string=input()
num=[int(n) for n in string.split()]
num=list(set(num))
print([num-1])