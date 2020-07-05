def function(l1, l2):
    count = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if pow(l1[i], l2[j]) > pow(l2[j], l1[i]):
                count += 1
    return count


n = int(input())
nums = []
string1 = []
string2 = []

for i in range(n):
    nums.append(input())
    string1.append(input())
    string2.append(input())

for i in range(n):
    ltemp1 = list(map(int, string1[i].split(' ')))
    ltemp2 = list(map(int, string1[i].split(' ')))
    
    print(function(ltemp1, ltemp2))

