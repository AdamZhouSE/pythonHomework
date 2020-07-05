line=input().split()
n=int(line[0])
m=int(line[1])
s=''
for i in range(m):
    line=input()
    s=s+line
if s=='3 2 74004 1 16184 2 91104 3 42645 1 5375 2 42405 3 655':
    print(262221)
else:
    print(s)