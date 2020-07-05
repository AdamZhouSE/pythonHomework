while True:
    s=(list)(input())
    if s[0]=="!":
        break
    else:
        oc=""
        for index in range(len(s)):
            if ord(s[index])>=ord("A") and ord(s[index])<=ord("Z"):
                oc=oc+chr(ord("Z")-ord(s[index])+ord("A"))
            elif ord(s[index])>=ord("a") and ord(s[index])<=ord("z"):
                oc=oc+chr(ord("z")-ord(s[index])+ord("a"))
            else:
                oc=oc+s[index]
        print(oc)