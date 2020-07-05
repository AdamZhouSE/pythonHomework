# 41
inp = input()
num = list(inp)
for i in range(len(num)):
    num[i] = int(num[i])
t = max(num)
print(max(num))

l = []
for i in range(t):
    st = []
    for j in range(len(num)):
        if num[j] >=1:
            num[j] -= 1
            st.append('1')
        else:
            st.append('0')
    l.append(int(''.join(st)))
l.sort(reverse = True)

outp = ''
for i in l:
    outp += str(i) + ' '
print(outp[:-1])