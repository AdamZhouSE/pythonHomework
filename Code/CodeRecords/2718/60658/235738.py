source = list(input())
li = input().replace("]","")
li = li.replace("[","")
li = [int(x) for x in li.split(",")]
for i in range(0,len(li),2):
    if source[li[i]]+source[li[i+1]]>source[li[i+1]]+source[li[i]]:
        source[li[i]],source[li[i+1]]=source[li[i+1]],source[li[i]]
print("".join(source))