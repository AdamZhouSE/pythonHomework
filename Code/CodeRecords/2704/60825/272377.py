s=input()
s.replace('[', ' ')
s.replace(']', ' ')
s.replace(',', ' ')
print(s)
l=s.split()
l= list(map(int, l))
print(l)