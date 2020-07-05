array = list(map(int, input()[1:-1].split(",")))
if len(array) <= 1:
    print(0)
gap = 0
for i in range(len(array)-1):
    if array[i+1]-array[i] > gap:
        gap = array[i+1] - array[i]
print(gap)