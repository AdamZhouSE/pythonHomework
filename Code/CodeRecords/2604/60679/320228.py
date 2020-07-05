def find(letters,target):
    for i in range(ord(target), ord('z') + 1):
        for j in range(len(letters)):
            if (i + 1 == ord(letters[j])):
                return letters[j]
    return letters[0]


read = input()
read = read[2:len(read)-2]
letters = read.split('", "')
target = input()
print(find(letters,target))