while True:
    s=input()
    if s=="!":break
    temp=""
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            temp+=chr(ord('z')-(ord(i)-ord('a')))
        elif ord('A') <= ord(i) <= ord('Z'):
            temp+=chr(ord('Z')-(ord(i)-ord('A')))
        else:temp+=i
    print(temp)
