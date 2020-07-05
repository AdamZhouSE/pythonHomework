# 将输入拆为区间的集合 如[['1','3'],['2','5']]
arr = input()
arr = arr[2:-2]
sections = [section for section in arr.split('],[')]
num = len(sections)  # 区间个数
index_of_intersections = []  # 交区间的位置

'''
    如果一个区间和它后面的区间有重叠区域,将前一个区间合并到后面的区间,则前面的区间无效,记录无效区间的位置,以此递推
'''
for i in range(num):
    for j in range(i+1,num):
        if int(sections[i].split(',')[1]) >= int(sections[j].split(',')[0]):
            sections[j] = sections[i].split(',')[0] + ',' + sections[j].split(',')[1]
            index_of_intersections.append(i)
            break

'''
    删除记录的无效区间
'''
for i in range(len(index_of_intersections)):
    sections.pop(index_of_intersections[i])
    for j in range(i+1,len(index_of_intersections)):  # 删除后, 后面区间的index-1
        index_of_intersections[j] -= 1

# 按照格式修改数组
for i in range(len(sections)):
    sections[i] = sections[i].split(',')[0] + ', ' + sections[i].split(',')[1]
arr = '[[' + '], ['.join(sections) + ']]'
print(arr)