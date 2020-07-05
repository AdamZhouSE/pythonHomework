s1 = input().strip()
s2 = input().strip()
pos = s1.find(s2, 0, len(s1))
while pos != -1:
    s1 = s1[0:pos] + s1[pos+len(s2):]
    # print(s1)
    pos = s1.find(s2, 0, len(s1))

print(s1)