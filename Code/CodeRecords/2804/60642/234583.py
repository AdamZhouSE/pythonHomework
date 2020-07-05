a=input()+'+'
b=c=0
list = []
out = ""
for i in a:
    if i=='+':
        list.append(int(c))
        c=0
    else :
        c = c * 10 + int(i)

for j in range(len(list)):
    out = out + str(min(list))+'+'
    list.remove(min(list))
out = out[0:-1]

print(out)