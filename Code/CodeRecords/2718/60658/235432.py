source = list(input())
string = input()[1:-1]
li = []
for i in string:
    if i.isdigit():
       li.append(int(i))
for i in range(0,len(li),2):
    if source[li[i]]+source[li[i+1]]>source[li[i+1]]+source[li[i]]:
        source[li[i]],source[li[i+1]]=source[li[i+1]],source[li[i]]
print("".join(source))