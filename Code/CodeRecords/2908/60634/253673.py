def equClass(w1,w2):
    tag = [0 for x in range(len(w1))]
    count = 0
    if len(w1) == len(w2):
        i = 0
        while i < len(w1):
            j = 0
            while j < len(w2):
                if w2[j] == w1[i] and tag[j] == 0:
                    tag[j] = 1
                    count += 1
                    break
                j += 1
            i += 1
        if count == len(w1):
            return True
        else:
            return False
    return False

def clasify(word,arr):
    i = 0
    while i <= len(arr):
        if i == len(arr):
            arr.append(word)
            break
        if equClass(word,arr[i]):
            break
        i += 1
        
num = int(input())
wClass = []
for x in range(num):
    clasify(input().split(" ")[0],wClass)
    
print(len(wClass),end="")
    

