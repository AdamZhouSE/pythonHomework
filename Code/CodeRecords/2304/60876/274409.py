class Queue:
    queue=[]
    def Queue(self):
        self.queue=[]
    def push(self,key):
        self.queue.append(key)
    def pop(self):
        k=self.queue[0]
        del self.queue[0]
        return k
n,root=map(int,input().split(" "))
nums=[]
index=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    nums.append([b,c])
    index.append(a)
sum=0
queue=Queue()
queue.push(root)
result=[]
while sum!=n:
    k=[]
    while queue.queue!=[]:
        now=queue.pop()
        k.append(now)
        sum+=1
    result.append(k)
    for item in k:
        ind=index.index(item)
        if nums[ind][0]!=0:
            queue.push(nums[ind][0])
        if nums[ind][1]!=0:
            queue.push(nums[ind][1])
length=len(result)
for i in range(0,length):
    print("Level {0} :".format(i+1),end="")
    for item in result[i]:
        print(" {0}".format(item),end="")
    print()
for i in range(0,length):
    if i%2==0:
        print("Level {0} from left to right:".format(i+1),end="")
        for item in result[i]:
            print(" {0}".format(item), end="")
    else:
        print("Level {0} from right to left:".format(i + 1), end="")
        l=len(result[i])
        for j in range(l-1,-1,-1):
            print(" {0}".format(result[i][j]),end="")
    print()