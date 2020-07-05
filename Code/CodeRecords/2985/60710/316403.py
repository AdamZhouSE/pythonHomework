stop=int(input())

i=1
string="A"
while True:
    if i==stop:
        break
    string=string+chr(ord('A')+i)+string
    i=i+1

print(string)