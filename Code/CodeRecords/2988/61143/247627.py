n = eval(input())
str = input()
m = eval(input())
s = list(str)
s_nm = []
for i in range(m-1,n):
    s_nm.append(s[i])
res = ''.join(s_nm)
print(res)