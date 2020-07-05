input = input()
buffer = []
for i in range(1,len(input)+1):
    buffer.append(input[len(input)-i:len(input)])
buffer.sort()
for j in range(len(input)):
    print(len(input)+1-len(buffer[j]),end='')
    if(j==len(input)-1):
        continue
    else:
        print(' ',end='')
print()