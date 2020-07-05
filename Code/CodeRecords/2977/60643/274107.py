line=input()
while line!="!":
    s=""
    for i in range(len(line)):
        if line[i].isalpha():
            if line[i].islower():
                diff=ord(line[i])-ord('a')
                s+=chr(ord('z')-diff)
            else:
                diff = ord(line[i]) - ord('A')
                s += chr(ord('Z') - diff)
        else:
            s+=line[i]
    print(s)
    line=input()