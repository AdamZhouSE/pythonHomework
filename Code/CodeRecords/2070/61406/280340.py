a = float(input())
b = int(input())
c = pow(a,b)
string = str(c)
index = string.index('.')
while len(string)-index<6:
    string = string+"0"
if len(string)-index>6:
    string = string[:index+6]
print(string)