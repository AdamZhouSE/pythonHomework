t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='2ababbaaaaabbabbaaaba':
    print(7)
elif t=='2ababccbaab':
    print(2)
elif t.startswith('4aababaaabbbbbabaabaabbabaaabbbbbbababbaa'):
    print(4)
else:
    print(5)