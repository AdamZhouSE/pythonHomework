s=input()
t=input()
print( "".join(sorted(list(t), key=lambda x: s.find(x))))