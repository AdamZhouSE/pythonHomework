string=input()
string2=""
for i in range(len(string)-1,-1,-1):
    string2+=string[i]
print(string2)