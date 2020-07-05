s1 = input()
s2 = input()
s3 = input()
s4 = input()

l1 = s3.split(" ")
l2 = s4.split(" ")
l3 = s2.split(" ")
num1 = int(l3[1])
num2 = int(l3[0])

l1.sort()
l2.sort()

if ord(l2[len(l2)-num1]) > ord(l1[num2-1]):
    print("YES")
else:
    print("NO")













