def countone(l):
    count = 0
    for i in range(len(l)):
        if l[i] == 1:
            count += 1
    return count


def convert(l, start, k):
    for i in range(start, start+k):
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
    return countone(l)


def reverse(s, k):
    num = []
    for i in range(len(s)-k+1):
        temp = []
        for m in range(len(s)):
            temp.append(int(s[m]))

        num.append(convert(temp, i, k))

    return max(num)


def countzero(l):
    count = 0
    for i in range(len(l)):
        if l[i] == '1':
            count += 1
    return count


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(s[i])

if countzero(l) == 0:
    print(len(l))
else:
    nums = []
    for i in range(len(l)):
        nums.append(reverse(''.join(l), i))
    
    #if max(nums) == 
    print(max(nums))

