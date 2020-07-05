head = input()
str_bin = ''
l = len(head)
for i in range(l-1):
    if(head[i]!='[')and(head[i]!=','):
        str_bin += head[i]
bin_res = int(str_bin,2)
print(bin_res)