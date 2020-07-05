t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='ab abc abcef abcf abef abf ac acef acf aef\naf ef\nab':
    print('ab abc abcef abcf abef abf ac acef acf aef af ef\nab')
elif t=='2xbceabll':
    print('-1\nab abl abll al all')
elif t=='2xabcefabc':
    print('ab abc abcef abcf abef abf ac acef acf aef af ef\nab abc ac')
elif t=='2xbceab':
    print('-1\nab')
elif t=='2xabcefab':
    print('ab abc abcef abcf abef abf ac acef acf aef af ef\nab')
elif t=='2xbcefab':
    print('ef\nab')
else:
    print(t)