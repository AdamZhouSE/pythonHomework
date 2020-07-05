def b(s1,s2):
    if len(s1)!=len(s2):
        print(1)
    elif s1==s2:
        print(2)
    elif s1.lower()==s2.lower():
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    b(input(),input())