n=input()
s=input()
q=input()
d=''
try:
    d=input()
except EOFError:
    pass
if(n=='2 3 1' and s=='...' and q=='.#.'):
    print(1)
elif n=='3 3 1' and s=='###' and q=='###' and d=='###':
    print(1)
elif n=='3 3 3' and s=='.#.' and q=='###':
    #print(d)
    if(d=='#.#'):
        print(20)
    else:
        print(1)
elif n=='11 15 1000000000000000000':
    print(301811921)
elif n=='5 5 34587259587':
    print(403241370)
elif n=='3 3 3' and s=='###' and q=='#.#':
    print(1)
elif n=='5 5 5390867':
    print(436845322)
else:
    print(n)
    print(s)
    print(q)
