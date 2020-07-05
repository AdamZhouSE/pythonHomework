import heapq
class PriorityQueue():
    def __init__(self):
        self._queue = []        #创建一个空列表用于存放队列
        self._index = 0        #指针用于记录push的次序
    
    def push(self, priority):
        """队列由（priority, index, item)形式的元祖构成"""
        heapq.heappush(self._queue, (-priority, self._index, priority)) 
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]    #返回拥有最高优先级的项
class Student():
    def __init__(self, score, scholarship):
        self.score = score
        self.scholarship = scholarship
    def get_score(self):
        return self.score
    def get_scholarship(self):
        return self.scholarship
def main():
    n,c,tot = input().split()
    students = []  #也可以是每个列表里有一堆元组 不能用字典 因为可能成绩有一样的
    for i in range(int(c)):
        score, scholarship = input().split()
        students.append(Student(int(score), int(scholarship)))
    students.sort(key= Student.get_score)  #排序算法
    f = []
    g = []
    for l in range(int(c)):
        f.append(0)
        g.append(0)
    q1 = PriorityQueue()
    q2 = PriorityQueue()
    sum = 0
    for j in range(int(int(n)/2)):
        q1.push(students[j].scholarship)
        sum = sum + students[j].scholarship
    k = int(int(n)/2)
    front = students[k:(int(c)-k)]
    for i, s in enumerate(front):  #s就是每一个student
        f[i+k] = sum
        num = q1.pop()
        if s.scholarship < num:
            sum = sum - num
            sum = sum + s.scholarship
            q1.push(s.scholarship)
        else:
            q1.push(num)
    sum = 0
    temp = students[(int(c)-int(int(n)/2)):]
    for m in range(len(temp)):
        q2.push(temp[m].scholarship)
        sum = sum + temp[m].scholarship
    for i, v in enumerate(reversed(front)):
        g[int(c)-i-k-1] = sum #这里g的下标可能存在问题
        num = q2.pop()
        if v.scholarship < num:
            sum = sum - num
            sum = sum + v.scholarship
            q2.push(v.scholarship)
        else:
            q2.push(num)
    result = []
    for p in range(int(c)-k):
        if p>=k and f[p]+g[p]+students[p].scholarship <= int(tot):
            result.append(students[p].score)
    if result != []:
        result.sort(reverse=True)
        oj = int(result[0])
        print(oj,end='')
    else:
        print(-1,end='')
    return
if __name__ == '__main__':
    main()