c=input()
c=int(c)
n = int(c ** 0.5)
left = 0
right = n
mark=0
while left <= right:
    tmp = left ** 2 + right ** 2
    if c == tmp:
        mark=1
        break
    if tmp < c:
        left += 1
    if tmp > c:
        right -= 1
if(mark==0):
    print("False")
else:
    print("True")