string=input()
num=0
for i in range(len(string)-2):
    if string[i]=="Q":
        for j in range(i+1,len(string)-1):
            if string[j]=="A":
                num+=string[j+1:].count("Q")
print(num,end='')