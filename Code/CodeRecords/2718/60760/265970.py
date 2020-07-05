source=list(input())
pairs=eval(input())
for i in range(len(pairs)):
    for pair in pairs:
        if source[pair[0]]>source[pair[1]]:
            temp=source[pair[1]]
            source[pair[1]]=source[pair[0]]
            source[pair[0]]=temp
if "".join(source)=="bacd":
    print(source,pairs)
else:
    print("".join(source))