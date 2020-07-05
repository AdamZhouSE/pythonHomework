n=eval(input())
string=input()
num=[int(n) for n in string.split()]
high=max(num)
result=0
for i in num:
    result=result+(high-i)
print(result)