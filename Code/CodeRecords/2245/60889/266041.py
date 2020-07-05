num = int(input())
longest = 0
now = 0
start = False
while num != 0:
    if start:
        if num%2==1:
            if now>longest:
                longest = now
            now = 1
            num = (num-1)/2
        else:
            num = num/2
            now = now + 1
    else:
        if num%2==1:
            start = True
            num = (num - 1)/2
            now = now + 1
        else:
            num = num / 2
print(longest)