def check(str2,k):
    count = 0
    for i in str2:
        if i == '0':
            count += 1
        if count > k:
            return False
    return  True

str1 = input()
str2 = input()
k =  int(input())
all = []
count = 0

for start in range(len(str2)):
    for end in range(start,len(str2)):
        tmp1 = str1[start:end+1]
        tmp2 = str2[start:end+1]
        if check(tmp2,k):
            if tmp1 not in all:
                all.append(tmp1)
                count += 1
        else:
            break
print(count)