s = input()
str=s.replace('[','').replace(']','')
num = str.split(',')
m = int(num[0])
n = int(num[1])
t = 0
while m != n:
    m >>= 1
    n >>= 1
    t += 1
print(n<<t)
