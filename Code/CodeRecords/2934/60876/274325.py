s=list(input())
result=""
ind=0
length=len(s)
listk=[]
class Stack:
    list1=[]
    top=-1
    def Stack(self):
        self.list1=[]
        self.top=-1
    def pop(self):
        self.top-=1
        k=self.list1[self.top+1]
        del self.list1[self.top+1]
        return k
    def push(self,i):
        self.top+=1
        self.list1.append(i)
stack=Stack()
for i in range(0,length):
    if s[i]=='[':
        stack.push(i)
    elif s[i]==']':
        c=stack.pop()
        ind=c+1
        num=""
        while s[ind].isdigit():
            num=num+s[ind]
            s[ind] = ""
            ind+=1
        if num=="":
            s[c]=""
            s[i]=""
        else:
            t = int(num)
            st = "".join(s[ind:i])
            s[c + 1] = (t - 1) * st
            s[c] = ""
            s[i] = ""
print("".join(s),end="")
