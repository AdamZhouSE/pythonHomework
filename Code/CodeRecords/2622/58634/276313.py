array = [int(i) for i in input().split(",")]
frequency = {}
for i in array:
    if not i in frequency.keys():
        frequency[i] = 1
    else:
        frequency[i] +=1
n = len(array)
limit = n//2
for i in array:
    if frequency[i] >limit:
        print(i)
        frequency[i] = 0
