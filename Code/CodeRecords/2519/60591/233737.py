s = input()
s = s.split('[')[1]
s = s.split(']')[0]
s = s.split(',')
s = list(map(int,s))
s.sort(reverse=True)
situation = True
for temp in range(len(s)-2):
    a = s[temp]
    b = s[temp+1]
    c = s[temp+2]
    if(a < b+c):
        situation = False
        print(a+b+c)
        break
if(situation):
    print(0)