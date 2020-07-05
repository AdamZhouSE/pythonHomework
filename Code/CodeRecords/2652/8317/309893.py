import heapq
class PriorityQueue():
    def __init__(self):
        self._queue = []        
        self._index = 0        
    
    def push(self, priority):
     
        heapq.heappush(self._queue, (-priority, self._index, priority)) 
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]    
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
    students = [] 
    for i in range(int(c)):
        score, scholarship = input().split()
        students.append(Student(int(score), int(scholarship)))
    students.sort(key= Student.get_score) 
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
    for i, s in enumerate(front): 
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
        g[int(c)-i-k-1] = sum 
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