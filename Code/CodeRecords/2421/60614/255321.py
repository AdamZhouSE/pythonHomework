init=input()
for i in range(len(init)):
    if init[i]=='6':
        init=init[0:i]+'9'+init[i+1:]
        break
print(init)