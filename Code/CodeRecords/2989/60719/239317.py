s1 = input()
s2 = input()
s3 = input()
m1 = s1
m2 = s2
m3 = s3
if s1 <= s2:
    if s3 <= s1:
        m1 = s3
        m2 = s1
        m3 = s2
    elif s3 <= s2:
        m2 = s3
        m3 = s2
else:
    if s3 >= s1:
        m1 = s2
        m2 = s1
    elif s3 >= s2:
        m1 = s2
        m2 = s3
        m3 = s1
    else:
        m1 = s3
        m3 = s1
print(m1)
print(m2)
print(m3)
