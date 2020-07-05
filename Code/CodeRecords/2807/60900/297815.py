s1 = input().split(' ')
s2 = input().split(' ')
s3 = input().split(' ')
l1 = int(s1[0])
l2 = int(s1[1])
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(0,l1):
    if int(s2[i]) % 2 == 0:
        count1+=1
    else:
        count2+=1
for i in range(0, l2):
    if int(s3[i]) % 2 == 0:
        count3 += 1
    else:
        count4 += 1

result =0
result = min(count1,count4)+min(count2,count3)
print(result)