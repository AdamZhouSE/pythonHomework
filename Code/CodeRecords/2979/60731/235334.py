s1, s2, s3, s4, s5 = input().split()
dic = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5}
index=1
length =len(s1)
for i in range(2,6):
    if len(dic[i])>length:
        index=i
        length=len(dic[i])
print(dic[index])
