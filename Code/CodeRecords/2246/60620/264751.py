import itertools
n=int(input())
judge=False
for num in itertools.permutations(str(n)):
    if(num[0]!='0'):
        if(bin(int(''.join(num)))).count('1')==1:
            judge=True
            break
print(judge)