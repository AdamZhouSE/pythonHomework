s1,s2,s3,s4,s5 = input().split()
s = [s1,s2,s3,s4,s5]
max_str = s1
for i in range(0,4):
    if len(s[i+1])>len(s[i]):
        max_str=s[i+1]

print(max_str)