s=input()
my_dic={}
l=[]

for i in range(len(s)):
    l.append(s[i:])
    my_dic[s[i:]]=i+1

l.sort()

for i in range(len(s)):
    print(my_dic[l[i]],end='')
    if i==len(s)-1:
        print()
    else:
        print(' ',end='')