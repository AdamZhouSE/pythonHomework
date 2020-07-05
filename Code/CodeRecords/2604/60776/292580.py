a=input()
a=a.replace("[\"","")
a=a.replace("\"]","")
b=a.split("\", \"")
zimu=input()
for i in range(1,26):
    if chr((ord(zimu)-ord('a')+i)%26+ord('a')) in b:
        print(chr((ord(zimu)-ord('a')+i)%26+ord('a')))
        break