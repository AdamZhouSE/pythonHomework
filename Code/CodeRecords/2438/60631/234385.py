input = input()
input = input[1:len(input)-1]
list = sorted(input.split(','))
out = []
for i in list:
    out.append(int(i))
print(out)              