source=list(input())
pairs=eval(input())
for i in range(len(pairs)^2):
    for pair in pairs:
        if source[pair[0]]>source[pair[1]]:
            temp=source[pair[1]]
            source[pair[1]]=source[pair[0]]
            source[pair[0]]=temp
print("".join(source))