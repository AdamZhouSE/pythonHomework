num = 0
s1 = input()
s2 = "CODEFESTIVAL2016"
for i  in range (16):
    if s1[i] == s2[i] :
        continue
    else:
        num = num +1
print(num)