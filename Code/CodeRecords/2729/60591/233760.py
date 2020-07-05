s = input().split("[")[1]
s = s.split("]")[0]
s = s.split(",")
s = list(map(int,s))
situation = True
for temp in range(0,len(s)-1,2):
    if(s[temp]!=s[temp+1]):
        situation = False
        print(s[temp])
        break

if(situation):
    print(s[-1])