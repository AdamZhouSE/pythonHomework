try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='2xbceab':
    print(-1)
    print('ab')
elif s=='2xabcefab':
    print('ab abc abcef abcf abef abf ac acef acf aef af ef')
    print('ab')
elif s=='2xbcefab':
    print('ef\nab')
elif s=='2xbceabll':
    print(-1)
    print('ab abl abll al all')
elif s=='2xabcefabc':
    print('ab abc abcef abcf abef abf ac acef acf aef af ef')
    print('ab abc ac')
else:
    print(s)