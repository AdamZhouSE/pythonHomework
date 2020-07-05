def atoi(s):
    s=s[::-1];
    num=0;
    for i,v in enumerate(s):
        offset=ord(v)-ord('0');
        num+=offset*(10**i);
    return num;
s=input("");
print(atoi(s));