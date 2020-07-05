num = int(input())
str1 = input().split(' ')
listleft = [int(i) for i in str1]
str2 = input().split(' ')
listvolum = [int(i) for i in str2]
adder = 0;
for i in listleft:
    adder=adder +i
listvolum.sort()
max1 = listvolum.pop()
max2 = listvolum.pop()
print("YES") if max1+max2>=adder else print("NO")