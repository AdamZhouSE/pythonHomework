def delete(string,target):
    for i in range(len(string)):
        for j in range(len(target)):
            if(target[j:j+1]==string[i:i+1]):
                target = target.replace(target[j:j+1],'-',1)
                string = string.replace(string[i:i+1],'.',1)
    return target



string = input()
read = input()
read = read[2:len(read)-2]
dictionary = read.split('","')
out = ""
for i in range(len(dictionary)):
    result = delete(string, dictionary[i])
    find = True
    for j in range(len(result)):
        if(result[j:j+1]!='-'):
            find = False
    if(find and len(out)<len(result)):
        out = dictionary[i]
print(out)