# 2
n = int(input())
outp = input()
for i in range(n-1):
    inp = input()
    ind = outp.find(inp[0])
    outp = outp[:ind] + inp + outp[ind+1:]
outp = outp.replace('*','')
print(outp,end ='')