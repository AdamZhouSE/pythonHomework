import itertools
n=int(input())
k=int(input())
num=[]
re=[]
for i in range(0,n):
    num.append(str(i+1))
s=itertools.permutations(num)
for j in s:
    re.append(j)
for letter in re[k-1]:
    print(letter,end="")
print()