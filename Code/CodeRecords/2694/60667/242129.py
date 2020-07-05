s = input()

l_pointer = 0
length = 0
maximum = ''

while l_pointer + length < len(s):
    if s[l_pointer:l_pointer+length] in s[l_pointer+1:]:
        length = length + 1
        maximum = s[l_pointer:l_pointer+length-1]
        continue
    else:
        l_pointer = l_pointer + 1

print(maximum)