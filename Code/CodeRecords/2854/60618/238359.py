n=[int(n) for n in input().split()]
print("Elephant")
if len(set(n))>3 or len(set(n))==1:
    print("Alien")
elif len(set(n))==2:
    