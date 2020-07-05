table = ['2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','#','7','7','8','8','8','9','9','9','#']

def transform(phoneNum):
    result = ""
    for x in phoneNum:
        if x <= 'Z' and x >= 'A':
            result += table[ord(x) - ord('A')]
        elif x >= '0' and x <= '9':
            result += x
    return result
    

def equal(phone1, phone2):
    if len(phone1) != len(phone2):
        return False
    for x in range(len(phone1)):
        if ord(phone1[x]) != ord(phone2[x]):
                return False
    return True

    
    

num = int(input())
phoneBook = []
for x in range(num):
    phoneBook.append(transform(input()))
    
diff = True
i = 0
while i < len(phoneBook) - 1:
    count = 1
    j = i + 1
    while j < len(phoneBook):
        if equal(phoneBook[i],phoneBook[j]):
            diff = False
            count += 1
            phoneBook.remove(phoneBook[j])
            j -= 1
        j += 1
    if count > 1:
        k = 0
        while k < len(phoneBook[i]):
            print(phoneBook[i][k],end = "")
            if k == 2:
                print('-',end = "")
            k += 1
        print(end = " ")
        print(count)
    i += 1

if diff:
    print("No duplicates.",end = "")
    
