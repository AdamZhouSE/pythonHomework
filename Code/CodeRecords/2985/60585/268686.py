def Building(n):
    if n==1:return 'A'
    else:return Building(n-1)+letters[n-1]+Building(n-1)

n=eval(input())
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(Building(n))