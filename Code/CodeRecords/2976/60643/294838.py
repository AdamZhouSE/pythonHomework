def operation(s,n,short):
    if short=="h":
        short=short.upper()
    if len(s) > 0:
        for i in range(len(s) - n):
            if s[i:i + n] == short:
                s = s[:i] + s[i + n:]
        if s.find(" ") != -1:
            s = s.replace(" ", "")
        print(s)
    else:
        print(s)

if __name__=="__main__":
    short=input()
    n=len(short)
    k=1
    s=input()
    while s!="}":
        operation(s,n,short)
        s=input()
    print("}")