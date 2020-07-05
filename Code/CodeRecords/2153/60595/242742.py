def Test():
    s = input()
    if (s.startswith("-")):
        s = s[1:]
        s = s[::-1]
        s="-"+zero(s)
    else:
        s = s[::-1]
        s=zero(s)
    print(s)

def zero(s):
    while(s.startswith("0")):
        s = s[1:]
    return s

if __name__ == "__main__":
    Test()