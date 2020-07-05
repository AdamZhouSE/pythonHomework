string = input()
i = 0
while i < len(string)-4:
    if string[i] == string[i+1] == string[i+2] == string[i+3] == string[i+4]:
        end = i+5
        while string[end] == string[i]:
            end = end + 1
            if end == len(string):
                break
        string = string[:i] + str(end-i)+"("+string[i]+")" + string[end:]
    i = i + 1
for i in range(2,int(len(string)/2)):
    j = 0
    while j < len(string)-2 * i+1:
        if string[j:j+i] == string[j+i:j+2*i]:
            end = j + 2 * i
            while string[end:end+i] == string[j:j+i]:
                end = end + i
                if end >= len(string):
                    break
            string = string[:j] + str(int((end-j)/i))+"("+string[j:j+i]+")" + string[end:]
        j = j + 1
print(len(string))