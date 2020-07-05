def findMinWords(target, words):
    sample = ''
    next = ''
    count = 0
    while len(sample) < len(target):
        found = False
        for i in range(len(sample)+1):
            smallTarget = target[len(sample)-i:]
            for w in words:
                if smallTarget.startswith(w):
                    next = w
                    found = True
                    break
            if found:
                if len(w) == i:
                    return -1
                sample = sample[:len(sample)-i] + w
                count += 1
                break
        if not found:
            return -1
        # print('w: %s'%w)
        # print('sample: %s'%sample)
    
    return count

n = int(input())
target = input()
words = []
for i in range(n):
    words.append(input())
words = sorted(words, key=len, reverse=True)
result = findMinWords(target, words)
print(result)
