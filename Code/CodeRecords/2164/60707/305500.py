
def de_duplication(str1):
    dedup_str = ''
    count = 0
    for char in str1:
        if not char in dedup_str:
            dedup_str += char
            count += 1
    
    return str(len(str1)-count)

n = int(input())
for i in range(n):
    str1 = input()
    print(de_duplication(str1))