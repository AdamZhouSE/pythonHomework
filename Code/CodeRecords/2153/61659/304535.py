n=int(input())
if n>=0:
    string=str(int(str(n)[::-1]))
    print(string)
else:
    string=str(n)[1:]
    string=str(int(string[::-1]))
    print(str(n)[0]+string)