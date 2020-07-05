"""
瓦莱拉是一个小男孩。 昨天他在学校里完成了一项艰巨的数学任务，因此瓦莱拉没有足够的时间正确学习英语字母表
不幸的是，英语老师决定今天对字母进行测试。 在测试中，瓦莱拉得到了一张 n*n 的方格纸，每个单位正方形包含英语字母的一些小写字母
瓦莱拉需要知道方形纸上书写的字母是否为字母“ X”。 瓦莱拉的老师认为，在下列情况下，纸上的字母形成“ X”：
在方格纸的两个对角线上，所有字母均相同；
纸张的所有其他正方形（它们不在对角线上）包含与对角线上的字母不同，但都是同一个字母。
帮助瓦莱拉，为他编写完成上述任务的程序
"""

n=int(input())-1
string_list = []

for i in range(n):
    string_list.append(list(str(input())))

result=True
X=(string_list[0])[0]
N=(string_list[0])[1]
if X==N:
    result=False

for i in range(len(string_list)):
    if X!=(string_list[i])[i] or X!=(string_list[i][n-i]) or (string_list[i])[i]!=(string_list[i][n-i]):
        result=False
    for m in range(len(string_list[i])):
        if m!=i and m!=n-i:
            if N!=(string_list[i])[m]:
                result=False

if result:
    print("YES")
else:
    print("NO")