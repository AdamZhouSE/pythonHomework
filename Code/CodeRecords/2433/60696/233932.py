arr = input()
arr = arr[2:-2]
sections = [section for section in arr.split('],[')]
num = len(sections)
num_of_intersections = 0
for i in range(num):
    for j in range(i+1,num):
        if int(sections[i].split(',')[1]) >= int(sections[j].split(',')[0]):
            sections[j] = sections[i].split(',')[0] + ',' + sections[j].split(',')[1]
            num_of_intersections = num_of_intersections + 1
            break
sections = sections[num_of_intersections:num]
for i in range(len(sections)):
    sections[i] = sections[i].split(',')[0] + ', ' + sections[i].split(',')[1]
arr = '[[' + '], ['.join(sections) + ']]'
print(arr)