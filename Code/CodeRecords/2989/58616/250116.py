s1 = input()
s2 = input()
s3 = input()
if s1 < s2:
    if s1 < s3:
        if s2 < s3:
            print(s1 + "\n" + s2 + "\n" + s3)
        else:
            print(s1 + "\n" + s3 + "\n" + s2)
    else:
        print(s3 + "\n" + s1 + "\n" + s2)
else:
    if s1 >= s3:
        if s2 >= s3:
            print(s3 + "\n" + s2 + "\n" + s1)
        else:
            print(s2 + "\n" + s3 + "\n" + s1)
    else:
        print(s2 + "\n" + s1 + "\n" + s3)