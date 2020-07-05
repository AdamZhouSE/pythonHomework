"""
小佩蒂娅在家里组织了一个新年聚会，邀请了 n 个朋友来,朋友间要互相交换礼物
她藏起了她的礼物，并观察朋友们相互送礼物
她记住了谁给谁礼物，且每个人都只获得了一个礼物
现在小佩蒂娅想知道每个朋友的礼物分别是谁送的，请你帮助她
"""

n=int(input())
arr=[int(k) for k in str(input()).split(" ")]

result=[0 for i in range(n)]

for i in range(len(arr)):
    result[arr[i]-1]=i+1

result=[str(k) for k in result]
print(" ".join(result))