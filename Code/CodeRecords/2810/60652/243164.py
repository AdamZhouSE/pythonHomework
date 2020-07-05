n = int(input())
l = list(int(i) for i in str(n))
print(max(l))
output = []
while any(l):
    b = ''
    for i in range(0,len(l)):
        if l[i] != 0:
            b += '1'
            l[i] -= 1
        else:
            b += '0'
    output.append(int(b))
print(" ".join(str(i) for i in output))